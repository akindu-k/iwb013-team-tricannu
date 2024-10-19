# TaskMate - AI-Powered Task Management System

Welcome to **TaskMate**, an innovative AI-powered solution designed to streamline task management and employee coordination. This system ensures tasks are assigned to the most suitable employees based on their skills and availability, helping organizations enhance productivity and simplify task workflows.

## Features

- **AI-Driven Task Assignment**: Tasks are assigned based on employee skills and availability using the Gemini-1.5-Flash AI model.
- **Multi-User Portals**: Separate dashboards for Admins, Managers, and Employees.
  - **Admin Dashboard**: Manage employee details (add, edit, and remove employees).
  - **Manager Dashboard**: Create tasks and view task assignments.
  - **Employee Dashboard**: View assigned tasks.
- **Trello Integration**: Option to import tasks from Trello boards directly into TaskMate.
- **Ballerina-Python Flask Integration**: Seamless communication between frontend and backend services, ensuring real-time task updates.

## Tech Stack

- **Frontend**: 
  - Built using **React**, **JSX**, and **CSS** for a modern and responsive UI.
  - **Vite** is used for efficient bundling and faster builds.

- **Backend**: 
  - The backend is powered by **Python Flask**.
  - **Ballerina** serves as the middleware connecting the frontend to the Flask backend and the AI model.
  
- **AI Model**: 
  - The **Gemini-1.5-Flash** AI model processes tasks and assigns them to employees based on their skills and availability.

## Getting Started

### Prerequisites
- **[Node.js](https://nodejs.org/en)** (for running the frontend)
- **[Python](https://www.python.org/)** (for the backend)
- **[Ballerina](https://ballerina.io/)** (for middleware integration)
- **[Gemini API](https://aistudio.google.com/app/apikey)** (export the Gemini API key before running the Python server)
- **[Trello API](https://developer.atlassian.com/cloud/trello/)** (optional, for Trello integration)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/akindu-k/iwb013-team-tricannu.git
    cd iwb013-team-tricannu
    ```

2. **Backend Setup**:
    - Navigate to the `backend` folder:
      ```bash
      cd backend
      ```
    - Before running the Python server, you need to export the **Gemini API Key**:
      ```bash
      export GEMINI_API_KEY=your-gemini-api-key
      ```

    - Run the Python backend:
      ```bash
      python3 index.py
      ```

3. **Ballerina Middleware Setup**:
    - Navigate to the `ballerina` folder:
      ```bash
      cd backend/ballerina
      ```
    - Start the Ballerina service:
      ```bash
      bal run main.bal
      ```

4. **Frontend Setup**:
    - Navigate to the `frontend` folder:
      ```bash
      cd frontend
      ```
    - Install frontend dependencies:
      ```bash
      npm install
      ```
    - Start the frontend:
      ```bash
      npm run dev
      ```

### Running the Application

Make sure to run each part of the application (Python server, Ballerina server, and frontend) in **three separate terminals** to keep all components running concurrently.

1. **Terminal 1**: Run the Python backend:
    ```bash
    cd backend
    python3 index.py
    ```

2. **Terminal 2**: Run the Ballerina middleware:
    ```bash
    cd backend/ballerina
    bal run main.bal
    ```

3. **Terminal 3**: Run the frontend:
    ```bash
    cd frontend
    npm run dev
    ```

### Usage

1. **Admin Portal**: Manage employees by adding, editing, or removing them.
2. **Manager Portal**: Create tasks and let the AI assign them to the most suitable employee.
3. **Employee Portal**: View and update assigned tasks.

### Screenshots

#### Homepage
_Add your homepage screenshot here._

#### Admin Dashboard
![Admin Dashboard](https://i.ibb.co/8Y6MNZ6/Screenshot-from-2024-10-20-01-55-47.png)

#### Manager Dashboard
![Manager Dashboard](https://i.ibb.co/qWYffjG/Screenshot-from-2024-10-20-01-59-20.png)

#### Employee Dashboard
![Employee Dashboard](https://i.ibb.co/BKvyfxS/Screenshot-from-2024-10-20-02-01-49.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- Akindu Kalhan - [akindu-k](https://github.com/akindu-k)

## Acknowledgements

- The TaskMate project was developed as part of the team **Tricannu** for the [Innovate with Ballerina](https://innovatewithballerina.com/).
