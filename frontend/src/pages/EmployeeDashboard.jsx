import React, { useState, useEffect } from 'react';
import axios from 'axios';

function EmployeeDashboard() {
  const [assignedTasks, setAssignedTasks] = useState('');

  useEffect(() => {
    const fetchAssignedTasks = async () => {
      try {
        const response = await axios.post('http://localhost:8080/taskDistributor/assignedTasks', {
          //"tasks": "Design a website for a magazine\nMake the monthly budget\nmake a cup of cofee\ndiscuss with the HR team about interns\nTrain the ML model\nMake a cup of tea"
          "tasks" : "Design a website for a magazine\nMake the monthly budget\nMake a cup of coffee\nDiscuss with the HR team about interns\nTrain the ML model\nMake a cup of tea\nOptimize the database for performance\nDevelop a marketing strategy for the new product launch\nConduct a security audit for the system\nPrepare a presentation for the board meeting\nCreate UI/UX wireframes for the mobile app\nUpdate the company's internal documentation\nSet up cloud infrastructure for the new service\nFix bugs in the frontend application\nOrganize a team-building event\nPrepare a monthly data analysis report\nCreate a user authentication system\nSchedule meetings with key stakeholders\nWrite a blog post for the company website\nTest the new features in the backend API"

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