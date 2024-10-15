import { useState } from 'react';
import './ContactUs.css';
import Navbar from './Navbar'; // Import the Navbar component

const ContactUs = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    country: '',
    company: '',
    jobRole: '',
    areaOfInterest: '',
    message: '',
    hearAbout: '',
    agreeToEmails: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log('Form Data Submitted:', formData);
  };

  return (
    <div>
      {/* Include the Navbar at the top of the page */}
      <Navbar />
      <div className="contact-us-container">
    
      <div className="contact-us">
        <h2>Contact Us</h2>
        <p>Please fill out the form, and we&apos;ll get in touch shortly.</p>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="text"
              name="firstName"
              placeholder="First Name *"
              value={formData.firstName}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="lastName"
              placeholder="Last Name *"
              value={formData.lastName}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <input
              type="email"
              name="email"
              placeholder="Email *"
              value={formData.email}
              onChange={handleChange}
              required
            />
            <input
              type="tel"
              name="phone"
              placeholder="Phone *"
              value={formData.phone}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <input
              type="text"
              name="country"
              placeholder="Country *"
              value={formData.country}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="company"
              placeholder="Company *"
              value={formData.company}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <input
              type="text"
              name="jobRole"
              placeholder="Job Role *"
              value={formData.jobRole}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="areaOfInterest"
              placeholder="Area of Interest *"
              value={formData.areaOfInterest}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <textarea
              name="message"
              placeholder="How Can We Help You?"
              value={formData.message}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <input
              type="text"
              name="hearAbout"
              placeholder="How Did You Hear About Us?"
              value={formData.hearAbout}
              onChange={handleChange}
            />
          </div>
          <div className="form-group checkbox-group">
            <label>
              <input
                type="checkbox"
                name="agreeToEmails"
                checked={formData.agreeToEmails}
                onChange={handleChange}
              />
              Yes, I would like to receive emails about new releases and updates.
            </label>
          </div>

          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
    </div>
  );
};

export default ContactUs;
