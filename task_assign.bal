import ballerina/io;
import ballerina/http;
import ballerina/system;
import ballerina/lang.runtime;

// Define an HTTP service on port 8080
service /taskAssign on new http:Listener(8080) {

    // Define an endpoint for assigning tasks
    resource function post assignTasks(http:Caller caller, http:Request req) returns error? {
        // Parse the incoming request body (task data from Trello)
        json payload = check req.getJsonPayload();
        io:println("Received tasks: ", payload.toJsonString());

        // Call the Python script to process the tasks and assign them
        string result = callPythonScript(payload.toJsonString());

        // Send back the result
        check caller->respond(result);
    }

    // Function to call the Python script using Ballerina's runtime API
    function callPythonScript(string jsonPayload) returns string {
        string pythonCmd = "python3";
        string scriptPath = "./src/task_distributor/assign_task.py"; // Path to your Python script
        
        // Pass the JSON data to the Python script via command line argument
        string[] args = [scriptPath, jsonPayload];

        // Execute the Python script
        runtime:Process process = new(pythonCmd, args);
        runtime:ProcessResult processResult = check process.waitForExit();

        // Capture the output from the Python script
        string stdout = processResult.getStdout();
        io:println("Python Output: ", stdout);

        return stdout;
    }
}
