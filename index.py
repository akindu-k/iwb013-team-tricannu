import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Sample employee data
employees = """[
    { "name": "Alice", "skills": ["UI Design", "Frontend Development"], "availability": True },
    { "name": "Bob", "skills": ["Backend Development", "Database Management"], "availability": True },
    { "name": "Charlie", "skills": ["Data Analysis", "Machine Learning"], "availability": False },
    { "name": "Diana", "skills": ["Project Management", "UI Design"], "availability": True }
]"""

with open("assigned_tasks.txt", "r") as f:
    taskList = ""
    task = f.readline().strip()
    while (task != ""):
        taskList += task + "\n"
        task = f.readline().strip()
        
    # print("Task:", task)
    prompt = "This is an employee set and tasklist. Assign the each task to the most suitable employee.\n" + employees + "\nTask: " + taskList
    response = model.generate_content(prompt)
    print(response.text)
