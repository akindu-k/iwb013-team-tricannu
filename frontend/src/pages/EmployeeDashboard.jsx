import { useState, useEffect } from 'react';
import axios from 'axios';
import './EmployeeDashboard.css';  // Import the updated CSS file

function EmployeeDashboard() {
  const [assignedTasks, setAssignedTasks] = useState([]);

  useEffect(() => {
    const fetchAssignedTasks = async () => {
      try {
        const response = await axios.get('http://localhost:8080/taskDistributor/taskList');
        console.log('Assigned Tasks:', response.data.assigned_tasks); // Debugging statement
        setAssignedTasks(response.data.assigned_tasks);
      } catch (error) {
        console.error('Error fetching assigned tasks:', error);
      }
    };

    fetchAssignedTasks();
  }, []);

  return (
    <div className="employee-dashboard-container">
      <h1>Employee Dashboard</h1>
      {assignedTasks && assignedTasks.map((task, index) => (
        <p key={index} className="assigned-task">{task}</p>
      ))}
    </div>
  );
}

export default EmployeeDashboard;
