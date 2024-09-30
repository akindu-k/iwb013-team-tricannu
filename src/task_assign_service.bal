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
    json tasks = check fetchTrelloTasks(boardId);
    io:println("Trello Tasks: ", tasks);

    // Cast the tasks to a JSON array before iterating
    json[] taskArray = <json[]>tasks;

    // For each task, call the ML model and assign employees
    foreach var task in taskArray {
        json taskData = {
            "task_complexity": 2,
            "employee_skill": 3,
            "task_urgency": 2
        };

        // Call the Flask API to assign the task
        json assignedTask = check getEmployeeAssignment(taskData);
        io:println("Assigned Task: ", assignedTask);
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
function getEmployeeAssignment(json task) returns json|error {
    http:Client mlClient = check new ("http://localhost:5000");

    http:Response response = check mlClient->post("/predict", task);
    json result = check response.getJsonPayload();
    return result;
}