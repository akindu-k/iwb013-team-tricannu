package optaplanner;

import java.util.Arrays;
import java.util.List;

public class DataLoader {

    public static List<Employee> loadEmployeeData() {
        return Arrays.asList(new Employee("Alice"), new Employee("Bob"), new Employee("Charlie"));
    }

    public static List<Task> loadTaskData() {
        return Arrays.asList(new Task("Task1"), new Task("Task2"), new Task("Task3"));
    }
}
