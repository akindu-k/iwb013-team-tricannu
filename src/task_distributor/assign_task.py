# import os
# import requests
# from employee_data import employees  # Assuming employees data is imported from this module
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Fetch Hugging Face API key from environment variables
# huggingface_api_key = os.getenv("HUGGING_FACE_API_KEY")
# trello_api_key =  os.getenv("TRELLO_API_KEY")
# trello_api_token = os.getenv("TRELLO_API_TOKEN")
# # Function to assign tasks using Hugging Face GPT-NeoX-20B
# def assign_tasks_to_employees(tasks):
#     assigned_tasks = []
#     employee_names = [employee['name'] for employee in employees]

#     for task in tasks:
#         task_description = task["name"]

#         # Create the prompt for GPT-NeoX-20B
#         prompt = (
#             f"Assign this task to the most suitable employee from the list based on their skills and availability. "
#             f"Task: '{task_description}'. The employees are: {employees}. "
#             "Respond with 'Assigned to: [Employee Name]' at the end."
#         )

#         # Use Hugging Face's API to get a response
#         response = requests.post(
#             "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B",
            
#             headers={"Authorization": f"Bearer {huggingface_api_key}"},
#             json={"inputs": prompt}
#         )

#         if response.status_code == 200:
#             result = response.json()

#             # Extract employee name from the result
#             print("Model response:", result)  # Debugging: print the raw model response

#             if isinstance(result, list) and result:
#                 assigned_text = result[0].get('generated_text', '')

#                 if "Assigned to:" in assigned_text:
#                     assigned_employee = assigned_text.split("Assigned to:")[-1].strip().split('.')[0]
#                 else:
#                     assigned_employee = "Assignment not found."
#             else:
#                 assigned_employee = "Invalid model response."
#         else:
#             assigned_employee = f"Error: {response.status_code} - {response.text}"

#         assigned_tasks.append({
#             "task": task_description,
#             "assigned_to": assigned_employee
#         })

#     return assigned_tasks

# # Function to fetch tasks from Trello
# def fetch_trello_tasks(board_id):
#     url = f"https://api.trello.com/1/boards/{board_id}/cards?key={trello_api_key}&token={trello_api_token}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching tasks from Trello: {response.status_code} - {response.text}")
#         return []

# # Main function
# def main():
#     board_id = "724STSoC"  # Your Trello Board ID

#     # Fetch tasks from Trello
#     tasks = fetch_trello_tasks(board_id)
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
































# import openai
# import requests
# from employee_data import employees  # Assuming you have the employee data in this module

# # OpenAI API key configuration
# openai.api_key = "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"


# # Sample employee data (use the actual import or replace this with the actual data)
# # employees = [
# #     {"name": "Alice", "skills": ["UI Design", "Frontend Development"], "availability": True},
# #     {"name": "Bob", "skills": ["Backend Development", "Database Management"], "availability": True},
# #     {"name": "Charlie", "skills": ["Data Analysis", "Machine Learning"], "availability": False},
# #     {"name": "Diana", "skills": ["Project Management", "UI Design"], "availability": True}
# # ]

# # Function to fetch tasks from Trello
# def fetch_trello_tasks(board_id, api_key, api_token):
#     url = f"https://api.trello.com/1/boards/{board_id}/cards?key={api_key}&token={api_token}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching tasks from Trello: {response.status_code} - {response.text}")
#         return []

# # Function to assign tasks to employees using GPT-4
# def assign_tasks_to_employees(tasks):
#     assigned_tasks = []
#     for task in tasks:
#         task_description = task["name"]
#         prompt = f"""
#         You are an AI assistant helping assign tasks to the most suitable employees.
#         Employees: {employees}
#         Task: {task_description}
#         Based on their skills and availability, assign the task to an appropriate employee.
#         """
        
#         # Call GPT-4 API
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant for assigning tasks."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
        
#         # Handle the response and extract the assigned employee
#         if response.choices:
#             assigned_employee = response.choices[0].message['content'].strip()
#         else:
#             assigned_employee = "No assignment generated."

#         assigned_tasks.append({
#             "task": task_description,
#             "assigned_to": assigned_employee
#         })
    
#     return assigned_tasks

# # Main function
# def main():
#     # Trello API credentials
#     trello_api_key = "109ad02b1fa4ffb3099672b18dd89b1f"
#     trello_api_token = "ATTA93269dd615a09a09487588c648873fb94bbb5bbeafedec6bf5a6e831b4f687e9EA8909C0"
#     board_id = "724STSoC"  # Your Trello Board ID

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


























# import openai
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Retrieve API key from environment variable
# openai_api_key = os.getenv("OPENAI_API_KEY")

# # Check if API key is loaded
# if openai_api_key is None:
#     raise ValueError("OpenAI API key not found in .env file.")

# # Sample employee data
# employees = [
#     {"name": "Alice", "skills": ["UI Design", "Frontend Development"], "availability": True},
#     {"name": "Bob", "skills": ["Backend Development", "Database Management"], "availability": True},
#     {"name": "Charlie", "skills": ["Data Analysis", "Machine Learning"], "availability": False},
#     {"name": "Diana", "skills": ["Project Management", "UI Design"], "availability": True}
# ]

# # Function to assign tasks using GPT-3.5-turbo
# def assign_tasks_to_employees(tasks):
#     assigned_tasks = []
    
#     for task in tasks:
#         task_description = task["name"]
        
#         prompt = f"""
#         Given the following task: "{task_description}", and these employees with their skills and availability:
#         {employees}. Assign the task to the most suitable available employee based on their skills.
#         """
        
#         # Make request to OpenAI API using GPT-3.5-turbo
#         try:
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # Use GPT-3.5-turbo or GPT-4
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": prompt}
#                 ],
#                 max_tokens=150,
#                 n=1,
#                 temperature=0.5,
#                 api_key=openai_api_key  # Pass the API key
#             )

#             # Extract the generated text
#             assigned_employee = response.choices[0].message['content'].strip()

#             assigned_tasks.append({
#                 "task": task_description,
#                 "assigned_to": assigned_employee
#             })
        
#         except Exception as e:
#             print(f"Error with OpenAI API request: {e}")
#             assigned_tasks.append({
#                 "task": task_description,
#                 "assigned_to": "Error"
#             })
    
#     return assigned_tasks

# # Example tasks to be assigned
# tasks = [
#     {"name": "Design the user interface for the new project."},
#     {"name": "Set up the database schema."},
#     {"name": "Analyze the customer data for trends."},
#     {"name": "Manage the project timelines and deliverables."}
# ]

# # Main function
# def main():
#     # Assign tasks to employees
#     assigned_tasks = assign_tasks_to_employees(tasks)
    
#     # Display the assigned tasks
#     for assignment in assigned_tasks:
#         print(f"Task: {assignment['task']}, Assigned To: {assignment['assigned_to']}")

# if __name__ == "__main__":
#     main()


























# import requests
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Retrieve Hugging Face API key from environment variable
# hf_api_key = os.getenv("HUGGING_FACE_API_KEY")

# # Check if API key is loaded
# if hf_api_key is None:
#     raise ValueError("Hugging Face API key not found in .env file.")

# # Sample employee data
# employees = [
#     {"name": "Alice", "skills": ["UI Design", "Frontend Development"], "availability": True},
#     {"name": "Bob", "skills": ["Backend Development", "Database Management"], "availability": True},
#     {"name": "Charlie", "skills": ["Data Analysis", "Machine Learning"], "availability": False},
#     {"name": "Diana", "skills": ["Project Management", "UI Design"], "availability": True}
# ]

# # Function to assign tasks using Hugging Face API
# def assign_tasks_to_employees(tasks):
#     assigned_tasks = []
    
#     for task in tasks:
#         task_description = task["name"]
        
#         prompt = f"""
#         Task: "{task_description}"
#         Based on the following employees and their skills and availability:
#         Employees: {employees}.
#         Assign the task to the most suitable available employee. Ensure to return only the employee's name.
#         """
        
#         # Make request to Hugging Face API using a model
#         headers = {"Authorization": f"Bearer {hf_api_key}"}
#         data = {"inputs": prompt}
        
#         try:
#             response = requests.post(
#                 "https://api-inference.huggingface.co/models/EleutherAI/gpt-neox-20b",
#                 headers=headers, 
#                 json=data
#             )
#             response.raise_for_status()

#             # Extract the generated text
#             result = response.json()
#             if isinstance(result, list) and len(result) > 0:
#                 # Extract employee name from the generated text
#                 generated_text = result[0]['generated_text'].strip()
#                 assigned_employee = generated_text.split()[-1].replace("'", "").replace(".", "")  # Extract the last word, assuming it's the employee's name
#             else:
#                 assigned_employee = "No assignment generated."

#             assigned_tasks.append({
#                 "task": task_description,
#                 "assigned_to": assigned_employee
#             })
        
#         except requests.exceptions.RequestException as e:
#             print(f"Error with Hugging Face API request: {e}")
#             assigned_tasks.append({
#                 "task": task_description,
#                 "assigned_to": "Error"
#             })
    
#     return assigned_tasks

# # Example tasks to be assigned
# tasks = [
#     {"name": "make a website about ML"},
#     {"name": "Make the monthly budget"},
#     {"name": "make a cup of coffee"},
#     {"name": "discuss with the HR team about interns"},
#     {"name": "Train the ML model"},
#     {"name": "Make a cup of coffee"},
#     {"name": "tdxtxvj"}
# ]

# # Main function
# def main():
#     # Assign tasks to employees
#     assigned_tasks = assign_tasks_to_employees(tasks)
    
#     # Display the assigned tasks
#     for assignment in assigned_tasks:
#         print(f"Task: {assignment['task']}, Assigned To: {assignment['assigned_to']}")

# if __name__ == "__main__":
#     main()
