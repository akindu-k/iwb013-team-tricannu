import ballerina/io;
import ballerina/http;
import ballerina/os;
import ballerina/lang.stringutils as strings;

// Trello API credentials and base URL
string apiKey = os:getEnv("TRELLO_API_KEY");
string apiToken = os:getEnv("TRELLO_API_TOKEN");
string trelloApiBaseUrl = "https://api.trello.com/1";
string boardId = "724STSoC"; // Board ID from your Trello URL

// Sample employee data
type Employee record {
    string name;
    string[] skills;
    boolean availability;
};

Employee[] employees = [
    {name: "Alice", skills: ["UI Design", "Frontend Development"], availability: true},
    {name: "Bob", skills: ["Backend Development", "Database Management"], availability: true},
    {name: "Charlie", skills: ["Data Analysis", "Machine Learning"], availability: false},
    {name: "Diana", skills: ["Project Management", "UI Design"], availability: true}
];

// Main function to execute the task assignment
public function main() returns error? {
    // Ensure API key and token are set
    if (apiKey == "" || apiToken == "") {
        io:println("Error: API Key or Token is missing. Set them as environment variables.");
        return;
    }

    // Fetch the tasks from Trello
    json|error tasksResult = fetchTrelloTasks(boardId);
    if tasksResult is error {
        io:println("Failed to fetch tasks from Trello: ", tasksResult.toString());
        return;
    }

    json tasks = tasksResult;

    // Cast the tasks to a JSON array before iterating
    if tasks is json[] {
        foreach var task in tasks {
            string taskName = task.name.toString();
            io:println("Processing Task: ", taskName);

            // Prepare the task description for the ML model
            json taskData = {
                "task_name": taskName,
                "task_complexity": 2, // Example metric for task complexity
                "task_urgency": 2     // Example metric for task urgency
            };

            // Assign the task to an employee based on the ML model
            json|error assignedTaskResult = assignTaskToEmployee(taskData);
            if assignedTaskResult is error {
                io:println("Failed to assign task: ", assignedTaskResult.toString());
                continue;
            }

            json assignedTask = assignedTaskResult;
            io:println("Assigned Task: ", assignedTask);
        }
    } else {
        io:println("Unexpected response format from Trello API.");
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

// Simulated function to call the Hugging Face model API for task assignment
function assignTaskToEmployee(json taskData) returns json|error {
    // Create the prompt for Hugging Face API or a simulated task assignment process
    string prompt = string `Assign this task '${taskData.task_name}' to the most suitable employee based on skills and availability. Employees: ${employees.toString()}`;

    // Call Hugging Face API (Simulated here, replace with actual API call)
    http:Client hugFaceClient = check new ("https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-125M");
    json requestBody = {
        "inputs": prompt
    };

    // Send the request to Hugging Face API
    http:Request req = new;
    req.setJsonPayload(requestBody);
    req.setHeader("Authorization", "Bearer " + os:getEnv("HUGGING_FACE_API_KEY"));
    
    // Simulating the response from Hugging Face
    json simulatedResponse = {
        "generated_text": "Task '" + taskData.task_name.toString() + "' assigned to Bob"
    };

    // Extract the employee assignment from the response
    string responseText = simulatedResponse.generated_text.toString();
    string assignedEmployee = extractAssignedEmployee(responseText);

    return <json>{
        "task": <json>taskData.task_name,
        "assigned_to": assignedEmployee
    };
}

// Function to extract assigned employee name from the response text
function extractAssignedEmployee(string responseText) returns string {
        string[] parts = string:split(responseText, "assigned to");
        if parts.length() > 1 {
            string employeeName = parts[1].trim();
            return employeeName;
        }
    
    return "Assignment not found.";
}
