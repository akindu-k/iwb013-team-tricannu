import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
with open('task_assignment_model_large.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

# Sample employee data
employees = [
    {"name": "Alice", "skills": ["UI Design", "Frontend Development", "Website Design"], "availability": True},
    {"name": "Bob", "skills": ["Backend Development", "Database Management", "Database Schema Setup"], "availability": True},
    {"name": "Charlie", "skills": ["Data Analysis", "Machine Learning", "Data Trends Analysis"], "availability": False},
    {"name": "Diana", "skills": ["Project Management", "UI Design", "Project Timelines"], "availability": True}
]

# Task assignment function
def assign_task(task_description):
    # Transform the task description using the vectorizer
    task_vector = vectorizer.transform([task_description])

    # Predict the assigned employee based on the task description
    predicted_label = model.predict(task_vector)[0]
    
    # Debugging: Print the predicted label
    print(f"Predicted Label for '{task_description}': {predicted_label}")

    # Check for matching employee by name
    for employee in employees:
        if employee["name"].lower() == predicted_label.lower():
            if employee["availability"]:
                return f"Task: {task_description}, Assigned To: {employee['name']}"
            else:
                return f"Task: {task_description}, Assigned To: {employee['name']} (Not available)"
    
    return f"Task: {task_description}, Assigned To: No suitable employee found."

# Example tasks to assign
tasks = [
    "Design a new website",
    "Set up the database schema",
    "Analyze customer data for trends",
    "Manage the project timelines and deliverables"
]

# Assign tasks
for task in tasks:
    result = assign_task(task)
    print(result)
