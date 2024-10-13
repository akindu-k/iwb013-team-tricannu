import { useState } from 'react';
import './ListTasks.css';  // Importing the ListTasks-specific CSS
import axios from 'axios';

const ListTasks = () => {
  const [tasks, setTasks] = useState([]);
  const [taskInput, setTaskInput] = useState('');

  const handleTaskInputChange = (e) => {
    setTaskInput(e.target.value);
  };

  const handleSubmit = () => {
    if (taskInput.trim() !== '') {
      setTasks([...tasks, taskInput]);
      setTaskInput(''); // Clear input after adding
    }
  };

  const handleDelete = (index) => {
    const updatedTasks = tasks.filter((task, taskIndex) => taskIndex !== index);
    setTasks(updatedTasks); // Update tasks list after deletion
  };

  const handleSubmitToBackend = async () => {
    console.log('Tasks:', tasks); // Debugging statement
    // Add code to send tasks to the backend
    const response = await axios.post('http://localhost:8080/taskDistributor/assignedTasks', {"tasks": tasks});
    console.log('Response:', response.data); // Debugging statement
  }

  return (
    <div className="list-tasks-container">
      <h2>List Tasks</h2>
      <p>Add tasks one by one by pressing Submit.</p>
      <div className="input-group">
        <input
          type="text"
          value={taskInput}
          onChange={handleTaskInputChange}
          placeholder="Enter a task"
          className="task-input"
        />
        <button onClick={handleSubmit} className="submit-button">Submit</button>
      </div>
      <ul className="task-list">
        {tasks.map((task, index) => (
          <li key={index} className="task-item">
            {task}
            <span className="delete-button" onClick={() => handleDelete(index)}>x</span>
          </li>
        ))}
      </ul>
      <button onClick={handleSubmitToBackend} className="submit-backend-button">Submit to Backend</button>

    </div>
  );
};

export default ListTasks;