import React, { useState, useEffect } from 'react';
import axios from 'axios';

function EmployeeDashboard() {
  const [assignedTasks, setAssignedTasks] = useState('');

  useEffect(() => {
    const fetchAssignedTasks = async () => {
      try {
        const response = await axios.post('http://localhost:8080/taskDistributor/assignedTasks', {
          "tasks": "Task1\nTask2\nTask3" // Example tasks
        });
        console.log('Assigned Tasks:', response.data.assigned_tasks); // Debugging statement
        setAssignedTasks(response.data.assigned_tasks);
      } catch (error) {
        console.error('Error fetching assigned tasks:', error);
      }
    };

    fetchAssignedTasks();
  }, []);

  return (
    <div>
      <h1>Employee Dashboard</h1>
      <pre>{assignedTasks}</pre>
    </div>
  );
}

export default EmployeeDashboard;