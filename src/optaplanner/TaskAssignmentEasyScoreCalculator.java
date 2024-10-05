import org.optaplanner.core.api.score.buildin.hardsoft.HardSoftScore;
import org.optaplanner.core.impl.score.director.easy.EasyScoreCalculator;

public class TaskAssignmentEasyScoreCalculator implements EasyScoreCalculator<TaskAssignmentSolution> {

    @Override
    public HardSoftScore calculateScore(TaskAssignmentSolution solution) {
        int hardScore = 0;
        int softScore = 0;

        // Simple scoring logic: just ensuring each task is assigned to an employee
        for (TaskAssignment assignment : solution.getAssignments()) {
            if (assignment.getEmployee() == null) {
                hardScore -= 1;  // Penalize unassigned tasks
            }
        }

        return HardSoftScore.of(hardScore, softScore);
    }
}
