package optaplanner;

import org.optaplanner.core.api.score.buildin.hardsoft.HardSoftScore;
import org.optaplanner.core.api.score.stream.Constraint;
import org.optaplanner.core.api.score.stream.ConstraintProvider;
import org.optaplanner.core.api.score.stream.ConstraintStream;

public class TaskAssignmentConstraintProvider implements ConstraintProvider {

    @Override
    public Constraint[] defineConstraints(ConstraintStream constraintFactory) {
        return new Constraint[]{
            // Define your constraints here, for example:
            assignTaskToSkilledEmployee(constraintFactory)
        };
    }

    private Constraint assignTaskToSkilledEmployee(ConstraintStream constraintFactory) {
        return constraintFactory
                .forEach(TaskAssignment.class)
                .filter(taskAssignment -> !taskAssignment.getEmployee().getSkills().contains(taskAssignment.getTask().getRequiredSkill()))
                .penalize("Employee doesn't have required skill", HardSoftScore.ONE_HARD);
    }
}
