@PlanningSolution
public class TaskAssignmentSolution {
    @PlanningEntityCollectionProperty
    private List<Task> taskList;
    @ValueRangeProvider(id = "employeeRange")
    private List<Employee> employeeList;
    
    @PlanningScore
    private HardSoftScore score;

    // Getters and setters
}
