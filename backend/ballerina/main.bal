import ballerina/http;


// Define the HTTP client to communicate with the Flask backend
http:Client backendClient = check new("http://localhost:5000");

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
        
        
        // Send the Flask response back to the frontend
        check caller->respond(backendResp.getJsonPayload());
    }
}

