import ballerina/http;
import ballerina/log;

service /taskAssign on new http:Listener(8080) {

    resource function post assignTasks(http:Caller caller, http:Request req) returns error? {
        // Retrieve the board ID from the request body
        json requestBody = check req.getJsonPayload();
        string boardId = requestBody.boardId.toString();

        // Call the Python script using a command-line interface
        string result = check runPythonScript(boardId);

        // Send the response back to the client
        check caller->respond(result);
    }

    // Function to run the Python script with the board ID as an argument
    function runPythonScript(string boardId) returns string|error {
        // Here, you can run your Python script using a command-line call
        // Adjust the command based on your environment
        string command = "python3 task_assign.py " + boardId;
        return runtime:exec(command);
    }
}
