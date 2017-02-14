public class constructer {
    private static void method(String name ) {
        System.out.println(name);
    }
    private static void method() {
        System.out.println("overrided fucntions");
    }
public static void main(String[] args) {
    String temp = "hello";
    method(temp);
}
}
