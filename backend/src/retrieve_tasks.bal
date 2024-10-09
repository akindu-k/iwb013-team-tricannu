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

    // Cast the tasks to a JSON array before iterating
    json[] taskArray = <json[]>tasks;

    // For each task, write the name to the text file
    foreach var _task in taskArray {
        check writeTaskNameToFile(_task);
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

//Function to write the task name to the text file
function writeTaskNameToFile(json task) returns error? {
    string filePath = "./assigned_tasks.txt";
    io:WritableByteChannel file = check io:openWritableFile(filePath, io:APPEND);

    // Extract the name member from the task JSON
    map<json> taskMap = check task.cloneWithType();
    string taskName = check taskMap["name"].toString();
    string taskDetails = taskName + "\n"; // Add a newline for better readability
    byte[] taskDetailsBytes = taskDetails.toBytes();
    var writeResult = check file.write(taskDetailsBytes, 0);

    check file.close();
    return;
}