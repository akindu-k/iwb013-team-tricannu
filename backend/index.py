import google.generativeai as genai
import os
from flask import Flask, request, jsonify

# Configure the Google Generative AI with your API key
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)

# Route for assigning tasks using POST
@app.route('/assign_tasks', methods=['POST'])
def assign_tasks():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Extract employee data and tasks from the JSON request body
    employees = data.get("employees", "")
    tasks = data.get("tasks", "")
    
    # Create the prompt for the model
    prompt = "This is an employee set and tasklist. Assign each task to the most suitable employee.\n" + employees + "\nTasks: " + tasks
    response = model.generate_content(prompt)
    
    # Return the AI model's response as JSON
    return jsonify({"assigned_tasks": response.text})

# Run the Flask server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
