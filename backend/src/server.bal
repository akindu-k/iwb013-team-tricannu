// // try to write task_assign.py in ballerina

// // frontend http request to bal server is similar to this
// const fetchdata= async () = {
//     const response = await axios.post("http://localhost:5000/task_assign", {task_id: 1, user_id: 1 });
//     console.log(response.data);
// }


// function callPythonChatbot(string message) returns json|error {
//     // Define the Python chatbot API URL
//     string pythonApiUrl = "http://localhost:5002";
//     json payload = {"message": message}; // Prepare the request payload

//     // Create a new HTTP client for the Python API
//     http:Client pythonClient = check new (pythonApiUrl);

//     // Log the payload to verify what is being sent
//     io:println("Sending payload to Python chatbot: ", payload.toString());

//     // Send a POST request to the Python chatbot
//     http:Response response = check pythonClient->post("/chatbot", payload);

//     // Log the entire response body as a string to see if it's valid JSON or not
//     string responseBody = (check (check response.getJsonPayload()).result).toString();

//     io:println("Raw response from Python chatbot: ", responseBody);

//     // Check if the response is JSON. If not, log an error message.
//     json jsonResponse;
//     if response.getContentType() == "application/json" {
//         // Parse the response to JSON only if it's of type application/json
//         jsonResponse = check (check response.getJsonPayload()).result;

//     } else {
//         io:println("Error: Received a non-JSON response from the Python server.");
//         return error("Non-JSON response: " + responseBody);
//     }

//     return jsonResponse;