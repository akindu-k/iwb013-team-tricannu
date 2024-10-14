import { useNavigate } from 'react-router-dom';
import './ManagerDashboard.css';  // Importing the Dashboard-specific CSS

const ManagerDashboard = () => {
  const navigate = useNavigate();

  return (
    <div className="dashboard-container">
      <h1>Manager Dashboard</h1>
      <div className="dashboard-section">
        <h2>Task Management</h2>
        <p>Click below to manage tasks.</p>
        <button onClick={() => navigate('/list-tasks')} className="dashboard-button">List Tasks</button>
      </div>
    </div>
  );
};

export default ManagerDashboard;
