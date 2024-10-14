import { Link } from 'react-router-dom';
import './Home.css'; // Import the styles for the home page

function Home() {
  return (
    <div className="home-container">
      <div className="welcome-section">
        <h1>Welcome to Task Allocator</h1>
        <p>Efficiently manage and assign tasks with ease.</p>
      </div>
      
      <div className="login-options">
        <h2>Select Your Role to Login</h2>
        <div className="role-buttons">
          <Link to="/login?role=employee" className="btn">Employee Login</Link>
          <Link to="/login?role=manager" className="btn">Manager Login</Link>
          <Link to="/login?role=admin" className="btn">Admin Login</Link>
        </div>
      </div>
    </div>
  );
}

export default Home;
