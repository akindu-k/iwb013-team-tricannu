import google.generativeai as genai
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# Configure the Google Generative AI with your API key
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

employees = []

@app.route('/employee_details', methods=['POST'])
def get_employee_details():
    global employees
    employees = request.json.get('employees', [])
    print(employees)
    return jsonify({"employees": employees})

# Route for getting assigned tasks
@app.route('/assign_tasks', methods=['POST'])
def get_assigned_tasks():
    taskList = request.json.get('tasks', [])
    taskListStr = '\n'.join(taskList)
    employee_details_str = ""
    
    for i in range(len(employees)):
        employee_details_str += str(employees[i]) + "\n"
    
    
    prompt = (
        "This is an employee set and tasklist. Assign each task to the most suitable employee. "
        "I want only the name and the assigned task. Remove bold, just the name and the task and nothing else. "
        "Add # as the delimiter to split one assignment from another. I need the answer in the following format: "
        "format: Alice - Develop a website#Bob - make a coffee. Don't add newline characters. "
        "Employees and tasks are as follows:\n"
        + employee_details_str + "\nTask: " + taskListStr
    )
    
    response = model.generate_content(prompt)
    return jsonify({"assigned_tasks": response.text})

# Run the Flask server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
