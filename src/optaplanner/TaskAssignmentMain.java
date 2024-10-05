package optaplanner;

import org.optaplanner.core.api.solver.SolverFactory;
import org.optaplanner.core.api.solver.Solver;

import java.util.List;

public class TaskAssignmentMain {

    public static void main(String[] args) {
        // Load the solver configuration from an XML file.
        SolverFactory<TaskAssignmentSolution> solverFactory = SolverFactory.createFromXmlResource("taskAssignmentSolverConfig.xml");

        // Create the solver
        Solver<TaskAssignmentSolution> solver = solverFactory.buildSolver();

        // Load employee data
        List<Employee> employeeList = DataLoader.loadEmployeeData();  // Assume DataLoader fetches employee data

        // Load task data
        List<Task> taskList = DataLoader.loadTaskData();  // Assume DataLoader fetches task data

        // Create the initial problem
        TaskAssignmentSolution unsolvedSolution = new TaskAssignmentSolution(employeeList, taskList);

        // Solve the problem
        TaskAssignmentSolution solvedSolution = solver.solve(unsolvedSolution);

        // Display the result
        for (TaskAssignment assignment : solvedSolution.getAssignments()) {
            System.out.println("Task: " + assignment.getTask().getName() +
                               " assigned to " + assignment.getEmployee().getName());
        }
    }
}
