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
            <h2>AI-Driven Task Assignment</h2>
            <p>
              TaskMate uses advanced machine learning models, such as Gemini 1.5
              Flash, to assign tasks based on employees&apos; skills,
              availability, and workload. This ensures that tasks are allocated
              efficiently, improving team productivity.
            </p>
          </div>

          <div className="about-section">
            <h2>Optimized Team Collaboration</h2>
            <p>
              Collaborate seamlessly within TaskMate. Keep track of your
              team&apos;s progress, share updates, and communicate through
              integrated tools that promote smooth workflow and coordination.
            </p>
          </div>

          <div className="about-section">
            <h2>Task Tracking & Analytics</h2>
            <p>
              Monitor your project milestones with real-time task tracking and
              analytics. TaskMate offers detailed reporting to help you make
              data-driven decisions and keep your projects on schedule.
            </p>
          </div>

          <div className="about-section">
            <h2>Trello Integration</h2>
            <p>
              TaskMate integrates with Trello, allowing you to manage and track
              your tasks within Trello boards while benefiting from
              TaskMate&apos;s AI-driven task assignment and reporting features.
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default OurServices;
