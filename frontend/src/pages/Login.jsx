import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import './Login.css'; // Import your login.css here
import Navbar from './Navbar';
function Login() {

    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [role] = useState(queryParams.get('role')); // Default role
  const navigate = useNavigate();

  console.log(role);

  const handleLogin = () => {
    // Mock authentication
    if (username && password) {
      if (role == 'admin') {
        navigate('/admin');
      } 
      else if (role == 'manager') {
        navigate('/list-tasks');
      } else {
        navigate('/employee');
      }
    } else {
      alert('Please enter valid credentials');
    }
  };

  return (
    <div className='login-main'>
      <Navbar />
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={(e) => e.preventDefault()}>
        <label>
          Username:
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
            required 
          />
        </label>
        <label>
          Password:
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
          />
        </label>
        <button type="button" onClick={handleLogin}>Login</button>
      </form>
    </div>
    </div>
  );
}

export default Login;
