import { useState } from 'react';
import './EmployeeDashboard.css'; // Import your CSS for styling

function EmployeeDashboard() {
  // State for storing tasks assigned to the employee
  const [tasks, setTasks] = useState([
    { id: 1, name: 'Complete report', done: false },
    { id: 2, name: 'Attend team meeting', done: false },
    { id: 3, name: 'Update project status', done: false },
  ]);

  // Function to mark task as done
  const handleTaskCompletion = (taskId) => {
    const updatedTasks = tasks.map(task => {
      if (task.id === taskId) {
        return { ...task, done: !task.done };
      }
      return task;
    });
    setTasks(updatedTasks);
  };

  return (
    <div className="employee-dashboard-container">
      <h1>Employee Dashboard</h1>
      <h2>Your Assigned Tasks</h2>

      <ul className="task-list">
        {tasks.length > 0 ? tasks.map(task => (
          <li key={task.id} className={task.done ? 'task done' : 'task'}>
            <span>{task.name}</span>
            <button 
              onClick={() => handleTaskCompletion(task.id)} 
              className={task.done ? 'done-btn' : 'complete-btn'}
            >
              {task.done ? 'Undo' : 'Mark as Done'}
            </button>
          </li>
        )) : (
          <p>No tasks assigned</p>
        )}
      </ul>
    </div>
  );
}

export default EmployeeDashboard;
