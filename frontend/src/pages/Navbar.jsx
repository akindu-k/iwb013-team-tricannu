import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Import the styles for the navbar

function Navbar() {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about">About Us</Link></li>
        <li><Link to="/services">Our Services</Link></li>
        <li><Link to="/contact">Contact Us</Link></li>
      </ul>
      <div className="logo-container">
        <img src="/src/assets/Leonardo_Phoenix_Create_a_modern_professional_logo_for_TaskMat_0-removebg-preview.png" alt="TaskMate Logo" className="logo" />
      </div>
    </nav>
  );
}

export default Navbar;
