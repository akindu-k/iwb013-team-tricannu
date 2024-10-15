import './About.css';
import Navbar from './Navbar';

const AboutUs = () => {
  return (
    <div>
        <Navbar />
    <div className="about-us-container">
        

      <div className="about-us-content">
        <section className="about-section">
          <h2>Our Mission</h2>
          <p>
            At TaskMaster, we are committed to streamlining the way teams assign and manage their tasks. Our goal is to help companies enhance productivity by offering an easy-to-use, efficient task management system that integrates with various team workflows.
          </p>
        </section>

        <section className="about-section">
          <h2>What We Do</h2>
          <p>
            TaskMaster provides intelligent task assignment using advanced machine learning models. Our platform analyzes team capabilities, deadlines, and task complexities to ensure optimal task distribution, helping teams meet their project goals.
          </p>
        </section>

        <section className="about-section">
          <h2>Our Story</h2>
          <p>
            Founded in 2021, TaskMaster started as a small project to solve the internal task management struggles of remote teams. Today, we serve hundreds of companies worldwide, providing a smarter and simpler solution to project management.
          </p>
        </section>


      </div>
    </div>
    </div>
  );
};

export default AboutUs;
