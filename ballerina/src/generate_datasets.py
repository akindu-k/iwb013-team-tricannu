import random
import pandas as pd

# Parameters
num_employees = 500
num_tasks = 100000

# Sample skills
skills_list = [
    "UI Design", "Frontend Development", "Backend Development", 
    "Database Management", "Data Analysis", "Machine Learning", 
    "Project Management", "Testing", "DevOps", "Cybersecurity"
]

# Generate employee data
employees = []
for emp_id in range(1, num_employees + 1):
    employee = {
        "Employee ID": emp_id,
        "Name": f"Employee {emp_id}",
        "Skills": random.sample(skills_list, k=random.randint(1, 5)),
        "Availability": random.choice([True, False])
    }
    employees.append(employee)

# Generate task data
tasks = []
for task_id in range(1, num_tasks + 1):
    task = {
        "Task ID": task_id,
        "Task Description": f"Task description for task {task_id}",
        "Required Skills": random.sample(skills_list, k=random.randint(1, 5))
    }
    tasks.append(task)

# Create DataFrames
employees_df = pd.DataFrame(employees)
tasks_df = pd.DataFrame(tasks)

# Save to CSV
employees_df.to_csv('employees_dataset.csv', index=False)
tasks_df.to_csv('tasks_dataset.csv', index=False)

print("Datasets generated and saved successfully!")
