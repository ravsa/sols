import java.io.*;

public class Employee {
    String name ;
    int age;
    String designation;
    double salary;
    public Employee(String name ) {
        this.name = name;
    }
    /**
     * set Employee age
     * @param age usage...
     *
     **/
    public void empAge(int age ) {
        this.age = age;
    }
    /**
     * set Employee salary
     * @param sal usage...
     *
     **/
    public void empSalary(double sal ){
        this.salary = sal;
    }
    /**
     * set designation of Employee
     * @param d usage...
     *
     **/
    public void setDesignation(String d ) {
        this.designation = d;
    }

    /**
     * show Employee details
     *
     **/
    public void printEmpDetails() {
        System.out.println("Name: " + this.name);
        System.out.println("Designation: " + this.designation);
        System.out.println("Age: " + this.age);
        System.out.println("Salary: " + this.salary);
        System.out.println("--------------------------------");
    }
}
