import java.io.*;

public class EmployeeTest {
    public static void main(String[] args) {
        Employee one = new Employee("Ravindra Singh");
        Employee two = new Employee("Rohit Kumawat");
        one.empAge(20);
        one.empSalary(290099);
        one.setDesignation("CEO");
        two.empAge(20);
        two.empSalary(290099);
        two.setDesignation("manager");
        one.printEmpDetails();
        two.printEmpDetails();

    }
}
