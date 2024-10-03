import ballerina/io;
import ballerina/http;
import ballerina/os;

string apiKey = os:getEnv("TRELLO_API_KEY");

string apiToken = os:getEnv("TRELLO_API_TOKEN");
string trelloApiBaseUrl = "https://api.trello.com/1";
string boardId = "724STSoC"; // Board ID from your Trello URL

public function main() returns error? {
    // Ensure API key and token are set
    if (apiKey == "" || apiToken == "") {
        io:println("Error: API Key or Token is missing. Set them as environment variables.");
        return;
    }

    // Fetch the tasks from Trello
    json tasksJson = check fetchTrelloTasks(boardId);
    json[] tasks = <json[]>tasksJson;

    //map<json> firstTask = <map<json>>tasks[0];
    //io:println("Trello Tasks: ", <string>firstTask["name"]);

    // Cast the tasks to a JSON array before iterating
    json[] taskArray = <json[]>tasks;

    // For each task, call the ML model and assign employees
    foreach var _task in taskArray {
        // json taskData = {
        //     "task_complexity": 2,
        //     "employee_skill": 3,
        //     "task_urgency": 2
        // };

        // Call the Flask API to assign the task
        json assignedTask = check writeToTextFile(_task);
        //io:println("Assigned Task: ", assignedTask);
    }
}

// Function to fetch tasks (cards) from a Trello board
function fetchTrelloTasks(string boardId) returns json|error {
    http:Client trelloClient = check new (trelloApiBaseUrl);
    string url = string `/boards/${boardId}/cards?key=${apiKey}&token=${apiToken}`;
    
    http:Response|error response = trelloClient->get(url);
    if response is http:Response {
        json result = check response.getJsonPayload();
        return result;
    } else {
        return error("Failed to fetch tasks from Trello");
    }
}

// Function to call the Flask ML model API to get task assignment
function writeToTextFile(json task) returns json|error {
    string filePath = "./assigned_tasks.txt";
    io:WritableByteChannel file = check io:openWritableFile(filePath, io:APPEND);

    string taskDetails = task.toString() + "\n"; // Add a newline for better readability
    byte[] taskDetailsBytes = taskDetails.toBytes();
    var writeResult = check file.write(taskDetailsBytes, 0);

    check file.close();
    return task;
}

