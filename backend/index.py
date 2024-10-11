# import google.generativeai as genai
# import os
# from flask import Flask, jsonify, request

# # Configure the Google Generative AI with your API key
# genai.configure(api_key=os.environ["API_KEY"])
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Initialize Flask app
# app = Flask(__name__)

# # Sample employee data
# employees = """[
#     { "name": "Alice", "skills": ["UI Design", "Frontend Development"], "availability": True },
#     { "name": "Bob", "skills": ["Backend Development", "Database Management"], "availability": True },
#     { "name": "Charlie", "skills": ["Data Analysis", "Machine Learning"], "availability": False },
#     { "name": "Diana", "skills": ["Project Management", "UI Design"], "availability": True }
# ]"""

# # Route for getting assigned tasks
# @app.route('/assign_tasks', methods=['POST'])
# def get_assigned_tasks():
#     taskList = request.json.get('tasks', '')
#     prompt = "This is an employee set and tasklist. Assign each task to the most suitable employee. I want only the name and the assigned task. Remove bold, just the name and the task and nothing else.\n" + employees + "\nTask: " + taskList
#     response = model.generate_content(prompt)
#     return jsonify({"assigned_tasks": response.text})

# # Run the Flask server on port 5000
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

    

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

# Sample employee data
employees = """[
    { "name": "Alice", "skills": ["UI Design", "Frontend Development"], "availability": True },
    { "name": "Bob", "skills": ["Backend Development", "Database Management"], "availability": True },
    { "name": "Charlie", "skills": ["Data Analysis", "Machine Learning"], "availability": False },
    { "name": "Diana", "skills": ["Project Management", "UI Design"], "availability": True }
]"""

# Route for getting assigned tasks
@app.route('/assign_tasks', methods=['POST'])
def get_assigned_tasks():
    taskList = request.json.get('tasks', '')
    prompt = ("This is an employee set and tasklist. Assign each task to the most suitable employee. "
              "I want only the name and the assigned task. Remove bold, just the name and the task and nothing else.\n"
              + employees + "\nTask: " + taskList)
    response = model.generate_content(prompt)
    return jsonify({"assigned_tasks": response.text})

# Run the Flask server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
