// OurServices.jsx
import "./OurServices.css";
import Navbar from "./Navbar";

const OurServices = () => {
  return (
    <>
      <Navbar />

      {/* Services Container */}
      <div className="about-us-container">
        {/* Banner Section */}
        <div className="about-us-banner">
          <h1>Our Services</h1>
        </div>

        {/* Main Content */}
        <div className="about-us-content">
          {/* Services Section */}
          <div className="about-section">
            <h2>Automated Task Assignment</h2>
            <p>
              Our AI-driven platform automatically assigns tasks to the
              best-suited team members based on skills, availability, and
              workload.
            </p>
          </div>

          <div className="about-section">
            <h2>Real-time Collaboration</h2>
            <p>
              Collaborate seamlessly with your team in real time. Share files,
              chat, and stay updated on task progress all in one place.
            </p>
          </div>

          <div className="about-section">
            <h2>Project Tracking & Reporting</h2>
            <p>
              Keep track of project milestones and generate reports to ensure
              smooth progress and informed decision-making.
            </p>
          </div>

          <div className="about-section">
            <h2>Third-party Tool Integration</h2>
            <p>
              We support integrations with tools like Trello, Slack, and Jira to
              give you a unified workflow experience.
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default OurServices;
