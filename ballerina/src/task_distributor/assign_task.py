import os
import requests
from employee_data import employees  # Assuming employees data is imported from this module
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch Hugging Face API key from environment variables
huggingface_api_key = os.getenv("HUGGING_FACE_API_KEY")
trello_api_key =  os.getenv("TRELLO_API_KEY")
trello_api_token = os.getenv("TRELLO_API_TOKEN")
# Function to assign tasks using Hugging Face GPT-NeoX-20B
def assign_tasks_to_employees(tasks):
    assigned_tasks = []
    employee_names = [employee['name'] for employee in employees]

    for task in tasks:
        task_description = task["name"]

        # Create the prompt for GPT-NeoX-20B
        prompt = (
            f"Assign this task to the most suitable employee from the list based on their skills and availability. "
            f"Task: '{task_description}'. The employees are: {employees}. "
            "Respond with 'Assigned to: [Employee Name]' at the end."
        )

        # Use Hugging Face's API to get a response
        response = requests.post(
            "https://api-inference.huggingface.co/models/EleutherAI/gpt-neox-20b",
            headers={"Authorization": f"Bearer {huggingface_api_key}"},
            json={"inputs": prompt}
        )

        if response.status_code == 200:
            result = response.json()

            # Extract employee name from the result
            print("Model response:", result)  # Debugging: print the raw model response

            if isinstance(result, list) and result:
                assigned_text = result[0].get('generated_text', '')

                if "Assigned to:" in assigned_text:
                    assigned_employee = assigned_text.split("Assigned to:")[-1].strip().split('.')[0]
                else:
                    assigned_employee = "Assignment not found."
            else:
                assigned_employee = "Invalid model response."
        else:
            assigned_employee = f"Error: {response.status_code} - {response.text}"

        assigned_tasks.append({
            "task": task_description,
            "assigned_to": assigned_employee
        })

    return assigned_tasks

# Function to fetch tasks from Trello
def fetch_trello_tasks(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/cards?key={trello_api_key}&token={trello_api_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching tasks from Trello: {response.status_code} - {response.text}")
        return []

# Main function
def main():
    board_id = "724STSoC"  # Your Trello Board ID

    # Fetch tasks from Trello
    tasks = fetch_trello_tasks(board_id)
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
