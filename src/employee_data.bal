import ballerina/http;

type Employee record {|
    string name;
    string[] skills;
    boolean availability;
|};

// Sample employee data
Employee[] employees = [
    { name: "Alice", skills: ["UI Design", "Frontend Development"], availability: true },
    { name: "Bob", skills: ["Backend Development", "Database Management"], availability: true },
    { name: "Charlie", skills: ["Data Analysis", "Machine Learning"], availability: false },
    { name: "Diana", skills: ["Project Management", "UI Design"], availability: true }
];

// Service to expose employee data
service /employee on new http:Listener(8080) {

    resource function get all() returns Employee[] {
        // Return the list of all employees
        return employees;
    }
}
