import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home'; // Import the new Home component
import Login from './pages/Login';
import EmployeeDashboard from './pages/EmployeeDashboard';
import AdminDashboard from './pages/AdminDashboard';
import ListTasks from './pages/ListTasks';
import ContactUs from './pages/ContactUs';
import About from './pages/About';
import './App.css';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/employee" element={<EmployeeDashboard />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/list-tasks" element={<ListTasks />} />
        <Route path="/contactus" element={<ContactUs />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;