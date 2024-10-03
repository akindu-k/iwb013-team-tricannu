import ballerina/time;

// Define a type for a Task
type Task record {
    string id;
    string description;
    string status;
    string assignedTo;
    time:Utc createdAt;
    time:Utc updatedAt?;
};

// Define a type for a User
type User record {
    string id;
    string name;
    string email;
    string role;
};

// Define a type for a Response
type Response record {
    string message;
    int code;
};

// Define a type for an Error
type Error record {
    string message;
    int code;
};

