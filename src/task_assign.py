# import os
# import requests
# import pickle
# from employee_data import employees  # Assuming employees data is imported from this module
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Fetch API keys from environment variables
# trello_api_key = os.getenv("TRELLO_API_KEY")
# trello_api_token = os.getenv("TRELLO_API_TOKEN")

# # Trello API endpoint to fetch lists from a board
# def fetch_lists_from_trello(board_id):
#     url = f"https://api.trello.com/1/boards/{board_id}/lists"
#     query = {
#         'key': trello_api_key,
#         'token': trello_api_token
#     }

#     response = requests.get(url, params=query)
#     if response.status_code == 200:
#         lists = response.json()  # Get the lists
#         return lists
#     else:
#         print(f"Error fetching lists from Trello: {response.status_code}")
#         return []

# # Trello API endpoint to fetch tasks (cards) from a specific list
# def fetch_tasks_from_trello(list_id):
#     url = f"https://api.trello.com/1/lists/{list_id}/cards"
#     query = {
#         'key': trello_api_key,
#         'token': trello_api_token
#     }

#     response = requests.get(url, params=query)
#     if response.status_code == 200:
#         tasks = response.json()  # Get the tasks (cards)
#         return tasks
#     else:
#         print(f"Error fetching tasks from Trello: {response.status_code}")
#         return []

# # Load the trained model and vectorizer
# def load_trained_model():
#     with open('task_assignment_model_large.pkl', 'rb') as f:
#         vectorizer, model = pickle.load(f)
#     return vectorizer, model

# # Function to assign tasks using the trained model
# def assign_tasks_to_employees(tasks):
#     assigned_tasks = []
#     employee_names = [employee['name'] for employee in employees]

#     # Load the trained model and vectorizer
#     vectorizer, model = load_trained_model()

#     for task in tasks:
#         task_description = task["name"]

#         # Transform the task description using the vectorizer
#         task_vector = vectorizer.transform([task_description])

#         # Predict the most suitable employee for the task
#         predicted_employee = model.predict(task_vector)[0]

#         # Ensure the predicted employee exists in the employee list
#         if predicted_employee in employee_names:
#             assigned_employee = predicted_employee
#         else:
#             assigned_employee = "No suitable employee found."

#         assigned_tasks.append({
#             "task": task_description,
#             "assigned_to": assigned_employee
#         })

#     return assigned_tasks

# # Main function to fetch tasks from a Trello board and assign them
# def main():
#     # Set your Trello board ID
#     board_id = "724STSoC"

#     # Fetch lists from the Trello board
#     lists = fetch_lists_from_trello(board_id)
#     if not lists:
#         print("No lists found in the Trello board.")
#         return

#     # Display lists and let the user pick one
#     print("Available lists on the board:")
#     for i, trello_list in enumerate(lists):
#         print(f"{i + 1}. {trello_list['name']} (ID: {trello_list['id']})")

#     # Prompt user to select a list by index
#     list_index = int(input("Enter the number of the list you want to fetch tasks from: ")) - 1
#     selected_list = lists[list_index]
#     list_id = selected_list['id']

#     print(f"Fetching tasks from the list: {selected_list['name']}")

#     # Fetch tasks from the selected list
#     tasks = fetch_tasks_from_trello(list_id)

#     if tasks:
#         # Assign tasks using the trained model
#         assigned_tasks = assign_tasks_to_employees(tasks)

#         # Print the assigned tasks
#         for assignment in assigned_tasks:
#             print(f"Task: {assignment['task']}, Assigned To: {assignment['assigned_to']}")
#     else:
#         print("No tasks found in the selected Trello list.")

# if __name__ == "__main__":
#     main()






























import os
import requests
import pickle
import sys
from src.employee_data import employees  # Assuming employees data is imported from this module
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API keys from environment variables
trello_api_key = os.getenv("TRELLO_API_KEY")
trello_api_token = os.getenv("TRELLO_API_TOKEN")

# Trello API endpoint to fetch lists from a board
def fetch_lists_from_trello(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    query = {
        'key': trello_api_key,
        'token': trello_api_token
    }

    response = requests.get(url, params=query)
    if response.status_code == 200:
        lists = response.json()  # Get the lists
        return lists
    else:
        print(f"Error fetching lists from Trello: {response.status_code}")
        return []

# Trello API endpoint to fetch tasks (cards) from a specific list
def fetch_tasks_from_trello(list_id):
    url = f"https://api.trello.com/1/lists/{list_id}/cards"
    query = {
        'key': trello_api_key,
        'token': trello_api_token
    }

    response = requests.get(url, params=query)
    if response.status_code == 200:
        tasks = response.json()  # Get the tasks (cards)
        return tasks
    else:
        print(f"Error fetching tasks from Trello: {response.status_code}")
        return []

# Load the trained model and vectorizer
def load_trained_model():
    with open('task_assignment_model_large.pkl', 'rb') as f:
        vectorizer, model = pickle.load(f)
    return vectorizer, model

# Function to assign tasks using the trained model
def assign_tasks_to_employees(tasks):
    assigned_tasks = []
    employee_names = [employee['name'] for employee in employees]

    # Load the trained model and vectorizer
    vectorizer, model = load_trained_model()

    for task in tasks:
        task_description = task["name"]

        # Transform the task description using the vectorizer
        task_vector = vectorizer.transform([task_description])

        # Predict the most suitable employee for the task
        predicted_employee = model.predict(task_vector)[0]

        # Ensure the predicted employee exists in the employee list
        if predicted_employee in employee_names:
            assigned_employee = predicted_employee
        else:
            assigned_employee = "No suitable employee found."

        assigned_tasks.append({
            "task": task_description,
            "assigned_to": assigned_employee
        })

    return assigned_tasks

# Main function to fetch tasks from a Trello board and assign them
def main():
    # Get the board ID from command line arguments
    if len(sys.argv) < 2:
        print("Please provide the Trello board ID as an argument.")
        return

    board_id = sys.argv[1]

    # Fetch lists from the Trello board
    lists = fetch_lists_from_trello(board_id)
    if not lists:
        print("No lists found in the Trello board.")
        return

    # Display lists and let the user pick one
    print("Available lists on the board:")
    for i, trello_list in enumerate(lists):
        print(f"{i + 1}. {trello_list['name']} (ID: {trello_list['id']})")

    # Prompt user to select a list by index
    list_index = int(input("Enter the number of the list you want to fetch tasks from: ")) - 1
    selected_list = lists[list_index]
    list_id = selected_list['id']

    print(f"Fetching tasks from the list: {selected_list['name']}")

    # Fetch tasks from the selected list
    tasks = fetch_tasks_from_trello(list_id)

    if tasks:
        # Assign tasks using the trained model
        assigned_tasks = assign_tasks_to_employees(tasks)

        # Print the assigned tasks
        for assignment in assigned_tasks:
            print(f"Task: {assignment['task']}, Assigned To: {assignment['assigned_to']}")
    else:
        print("No tasks found in the selected Trello list.")

if __name__ == "__main__":
    main()

