import "./About.css";
import Navbar from "./Navbar";

const AboutUs = () => {
  return (
    <div>
      <Navbar />
      <div className="about-us-container">
        <div className="about-us-content">
          <section className="about-section">
            <h2>Our Mission</h2>
            <p>
              At TaskMate, we are dedicated to revolutionizing task management
              by leveraging cutting-edge AI models. Our mission is to enhance
              team efficiency through intelligent task assignments that match
              employees&apos; skills and availability, reducing manual workload
              and ensuring productivity across teams.
            </p>
          </section>

          <section className="about-section">
            <h2>What We Do</h2>
            <p>
              TaskMate utilizes the power of the Gemini-1.5-Flash LLM to assign
              tasks to employees intelligently. Our platform evaluates team
              members&apos; skills, availability, and task requirements to
              provide the most efficient task distribution, improving project
              outcomes and team performance.
            </p>
          </section>

          <section className="about-section">
            <h2>Our Story</h2>
            <p>
              TaskMate was initiated on 1st September 2024 as part of the
              Innovate with Ballerina competition. What began as an effort to
              streamline task assignments using AI is now on a journey to offer
              something valuable to teams worldwide. We believe in creating
              tools that improve how people work, and TaskMate is here to
              deliver that.
            </p>
          </section>
        </div>
      </div>
    </div>
  );
};

export default AboutUs;
