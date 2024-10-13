import ballerina/http;
import ballerina/io;

string[] assignedtasksList= [];

http:Client selfClient = check new("http://localhost:8080");

// Define the HTTP client to communicate with the Flask backend
http:Client backendClient = check new("http://localhost:5000");
@http:ServiceConfig {
    cors: {
        allowOrigins: ["*"],
        allowHeaders: ["Content-Type"],
        allowMethods: ["GET", "POST", "OPTIONS"]
    }
}

// Define the Ballerina service
service /taskDistributor on new http:Listener(8080) {

    // POST method to handle task assignment
    resource function post assignedTasks(http:Caller caller, http:Request req) returns error? {
        // Get the JSON payload from the frontend request
        json reqBody = check req.getJsonPayload();
        
        // Create a new HTTP request to send to Flask
        http:Request backendReq = new;
        backendReq.setPayload(reqBody);
        
        // Send the request to the Flask backend and get the response
        http:Response backendResp = check backendClient->post("/assign_tasks", backendReq);

        backendResp.setHeader("Access-Control-Allow-Origin", "*"); // Adjust origin as needed
        backendResp.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
        backendResp.setHeader("Access-Control-Allow-Headers", "Content-Type");
        
        // io:println(backendResp.getJsonPayload());
        json assignedTasks = check backendResp.getJsonPayload();
        // assignedtasksList.push(assignedTasks);
        io:println(assignedTasks.assigned_tasks);

        string:RegExp r = re `#`;
        assignedtasksList = r.split(check assignedTasks.assigned_tasks);

        
        io:println(assignedtasksList);
        
        
        // Send the Flask response back to the frontend
        check caller->respond({assigned_tasks: assignedtasksList});
    }

    // GET method to return the list of assigned tasks
    resource function get taskList(http:Caller caller) returns error? {
        // Send the list of assigned tasks to the frontend
        check caller->respond({assigned_tasks: assignedtasksList});
    }

    // resource function post taskList(http:Caller caller, http:Request req) returns error? {
    //     json reqBody = check req.getJsonPayload();
    //     // io:println(reqBody.tasks);
    //     http:Request backendReq = new;
    //     backendReq.setPayload(reqBody);

    //     http:Response backendResp = check backendClient->post("/assign_tasks", backendReq);

    //     backendResp.setHeader("Access-Control-Allow-Origin", "*"); // Adjust origin as needed
    //     backendResp.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
    //     backendResp.setHeader("Access-Control-Allow-Headers", "Content-Type");
        
    //     // io:println(backendResp);
    //     json assignedTasks = check backendResp.getJsonPayload();
    //     assignedtasksList.push(assignedTasks);
    //     io:println(assignedtasksList);
        
    //     // Send the Flask response back to the frontend
    //     check caller->respond(backendResp.getJsonPayload());
    // }

}




