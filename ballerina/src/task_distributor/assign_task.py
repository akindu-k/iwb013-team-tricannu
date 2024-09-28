from employee_data import employees
import requests

# Sample employee data
# employees = [
#     {"name": "Alice", "skills": ["UI Design", "Frontend Development"], "availability": True},
#     {"name": "Bob", "skills": ["Backend Development", "Database Management"], "availability": True},
#     {"name": "Charlie", "skills": ["Data Analysis", "Machine Learning"], "availability": False},
#     {"name": "Diana", "skills": ["Project Management", "UI Design"], "availability": True},
# ]

# Function to fetch tasks from Trello
def fetch_trello_tasks(board_id, api_key, api_token):
    url = f"https://api.trello.com/1/boards/{board_id}/cards?key={api_key}&token={api_token}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

# Function to assign tasks using Hugging Face
def assign_tasks_to_employees(tasks):
    assigned_tasks = []
    for task in tasks:
        task_description = task["name"]
        prompt = f"Assign this task to an employee based on their skills and availability: {task_description}. Employees: {employees}"
        
        response = requests.post(
            "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-125M",
            headers={"Authorization": ""},
            json={"inputs": prompt},
        )
        
        # Handle the response
        if response.status_code == 200:
            result = response.json()
            # Extract the employee name directly from the result
            if isinstance(result, list) and result:
                assigned_text = result[0]['generated_text']
                # Attempt to extract the employee's name from the assigned text
                assigned_employee = assigned_text.split(":")[-1].strip().split('.')[0]  # Take the first part after the colon
            else:
                assigned_employee = "No assignment generated."
        else:
            assigned_employee = f"Error: {response.status_code} - {response.text}"
        
        assigned_tasks.append({
            "task": task_description,
            "assigned_to": assigned_employee
        })
    return assigned_tasks

# Main function
def main():
    # Trello API credentials
    trello_api_key = ""
    trello_api_token = ""
    board_id = ""  # Your Trello Board ID

    # Fetch tasks from Trello
    tasks = fetch_trello_tasks(board_id, trello_api_key, trello_api_token)
    if not tasks:
        print("No tasks found in Trello.")
        return

    # Assign tasks to employees
    assigned_tasks = assign_tasks_to_employees(tasks)
    
    # Display the assigned tasks
    for assignment in assigned_tasks:
        print(f"Task: {assignment['task']}, Assigned To: {assignment['assigned_to']}")

if __name__ == "__main__":
    main()

















# import requests
# from employee_data import employees  # Assuming employees data is imported from this module

# # Function to fetch tasks from Trello
# def fetch_trello_tasks(board_id, api_key, api_token):
#     url = f"https://api.trello.com/1/boards/{board_id}/cards?key={api_key}&token={api_token}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching tasks from Trello: {response.status_code} - {response.text}")
#         return []

# # Function to assign tasks using Hugging Face GPT-Neo
# def assign_tasks_to_employees(tasks):
#     assigned_tasks = []
#     for task in tasks:
#         task_description = task["name"]
#         prompt = f"Assign this task to an employee based on their skills and availability: {task_description}. Employees: {employees}"
        
#         # Updated to use a supported model like gpt-neo-2.7B
#         response = requests.post(
#             "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B",  # Use the supported model
#             headers={"Authorization": "Bearer "},  # Replace with your Hugging Face API key
#             json={"inputs": prompt},
#         )
        
#         # Handle the response
#         if response.status_code == 200:
#             result = response.json()
#             if isinstance(result, list) and result:
#                 # Debug: print the full response from the model
#                 print(f"Model Response: {result[0]['generated_text']}")
#                 assigned_text = result[0]['generated_text']

#                 # Extract the employee name from the response text
#                 assigned_employee = extract_employee_name(assigned_text, employees)
#             else:
#                 assigned_employee = "No assignment generated."
#         else:
#             assigned_employee = f"Error: {response.status_code} - {response.text}"
        
#         assigned_tasks.append({
#             "task": task_description,
#             "assigned_to": assigned_employee
#         })
#     return assigned_tasks

# # Helper function to extract employee name from the response text
# def extract_employee_name(generated_text, employees):
#     try:
#         # Instead of relying on the phrase "Assign this task to", let's check if any employee's name appears in the text
#         for employee in employees:
#             if employee['name'] in generated_text:
#                 return employee['name']
#         return "No valid employee found."
#     except Exception as e:
#         return f"Error extracting employee name: {str(e)}"

# # Main function
# def main():
#     # Trello API credentials (Do not hardcode credentials in production!)
#     trello_api_key = ""
#     trello_api_token = ""
#     board_id = ""  # Your Trello Board ID

#     # Fetch tasks from Trello
#     tasks = fetch_trello_tasks(board_id, trello_api_key, trello_api_token)
#     if not tasks:
#         print("No tasks found in Trello.")
#         return

#     # Assign tasks to employees
#     assigned_tasks = assign_tasks_to_employees(tasks)
    
#     # Display the assigned tasks
#     for assignment in assigned_tasks:
#         print(f"Task: {assignment['task']}, Assigned To: {assignment['assigned_to']}")

# if __name__ == "__main__":
#     main()


























