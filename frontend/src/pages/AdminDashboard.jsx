import { useState } from "react";
import "./AdminDashboard.css";
import Navbar from "./Navbar";
import axios from "axios";

export default function AdminDashboard() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [skills, setSkills] = useState("");
  const [availability, setAvailability] = useState("Available");
  const [isEditing, setIsEditing] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(null);

  const handleSubmitToBackend = async (updatedEmployees) => {
    try {
      const response = await axios.post(
        "http://localhost:8080/taskDistributor/employee_details",
        { employees: updatedEmployees }
      );
      console.log("response", response);
    } catch (error) {
      console.error("Error sending employee details to backend:", error);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newEmployee = { name, skills, availability };
    if (isEditing) {
      const employees = employees.map((employee, index) =>
        index === currentIndex ? newEmployee : employee
      );
      setEmployees(employees);
      setIsEditing(false);
      setCurrentIndex(null);
    } else {
      setEmployees((prevEmployees) => {
        const updatedEmployees = isEditing
          ? prevEmployees.map((employee, index) =>
              index === currentIndex ? newEmployee : employee
            )
          : [...prevEmployees, newEmployee];
        handleSubmitToBackend(updatedEmployees);
        return updatedEmployees;
      });
    }

    handleSubmitToBackend();
    setName("");
    setSkills("");
    setAvailability("Not Available");
  };

  const handleRemove = (index) => {
    const employees = employees.filter((_, i) => i !== index);
    setEmployees(employees);
  };

  const handleEdit = (index) => {
    const employee = employees[index];
    setName(employee.name);
    setSkills(employee.skills);
    setAvailability(employee.availability);
    setIsEditing(true);
    setCurrentIndex(index);
  };

  return (
    <div className="container">
      <Navbar />
      <h1 className="text-2xl font-bold mb-4">Admin Dashboard</h1>
      <div className="grid md:grid-cols-2">
        <div className="card">
          <div className="card-header">
            <h2 className="card-title">
              {isEditing ? "Edit Employee" : "Add Employee"}
            </h2>
          </div>
          <div className="card-content">
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label htmlFor="name" className="label">
                  Employee Name
                </label>
                <input
                  id="name"
                  className="input"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Enter employee name"
                  required
                />
              </div>
              <div>
                <label htmlFor="skills" className="label">
                  Skills
                </label>
                <input
                  id="skills"
                  className="input"
                  value={skills}
                  onChange={(e) => setSkills(e.target.value)}
                  placeholder="Enter skills (comma-separated)"
                  required
                />
              </div>
              <div>
                <label htmlFor="availability" className="label">
                  Availability
                </label>
                <div className="select-wrapper">
                  <select
                    id="availability"
                    className="select"
                    value={availability}
                    onChange={(e) => setAvailability(e.target.value)}
                  >
                    <option value="Available">Available</option>
                    <option value="Not Available">Not Available</option>
                  </select>
                </div>
              </div>
              <button type="submit" className="button">
                {isEditing ? "Update Employee" : "Add Employee"}
              </button>
            </form>
          </div>
        </div>
        <div className="card">
          <div className="card-header">
            <h2 className="card-title">Employee List</h2>
          </div>
          <div className="card-content">
            <table className="table">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Skills</th>
                  <th>Availability</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {employees.map((employee, index) => (
                  <tr key={index}>
                    <td>{employee.name}</td>
                    <td>{employee.skills}</td>
                    <td>{employee.availability}</td>
                    <td>
                      <div className="table-actions">
                        <button
                          onClick={() => handleEdit(index)}
                          className="button"
                        >
                          Edit
                        </button>
                        <button
                          onClick={() => handleRemove(index)}
                          className="button"
                        >
                          Remove
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
