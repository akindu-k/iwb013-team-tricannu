package optaplanner;


import org.optaplanner.core.api.domain.solution.PlanningSolution;
import org.optaplanner.core.api.domain.solution.PlanningEntityProperty;
import org.optaplanner.core.api.domain.valuerange.ValueRangeProvider;
import org.optaplanner.core.api.domain.solution.PlanningScore;
import org.optaplanner.core.api.score.buildin.hardsoft.HardSoftScore;

import java.util.List;

@PlanningSolution
public class TaskAssignmentSolution {

    private List<Employee> employeeList;
    private List<Task> taskList;
    private List<TaskAssignment> assignments;
    private HardSoftScore score;

    // Constructors, getters, and setters

    public TaskAssignmentSolution(List<Employee> employeeList, List<Task> taskList) {
        this.employeeList = employeeList;
        this.taskList = taskList;
    }

    @ValueRangeProvider(id = "employeeRange")
    public List<Employee> getEmployeeList() {
        return employeeList;
    }

    @PlanningEntityProperty
    public List<TaskAssignment> getAssignments() {
        return assignments;
    }

    public void setAssignments(List<TaskAssignment> assignments) {
        this.assignments = assignments;
    }

    @PlanningScore
    public HardSoftScore getScore() {
        return score;
    }

    public void setScore(HardSoftScore score) {
        this.score = score;
    }
}
