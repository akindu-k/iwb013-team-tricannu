import pandas as pd
from data_preprocessing import load_data, preprocess_data
from model import TaskAssignmentModel

def main():
    # Load and preprocess the data
    df = load_data('data/large_task_assignments.csv')
    df = preprocess_data(df)

    # Split the data into features and labels
    X = df['task']  # Task descriptions
    y = df['assigned_to']  # Employee names

    # Train the model
    model = TaskAssignmentModel()
    model.train(X, y)

    # Save the model
    model.save_model('models/task_assignment_model.pkl')

    # Example predictions
    tasks_to_assign = ["Make a cup of coffee", "Design a machine learning model"]
    for task in tasks_to_assign:
        assigned_employee = model.predict(task)[0]
        print(f'Task: {task}, Assigned To: {assigned_employee}')

if __name__ == "__main__":
    main()
