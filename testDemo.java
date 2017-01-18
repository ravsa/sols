public class testDemo {
    private static testDemo instance = null;
    private testDemo(){}
    public static testDemo getInstance(){
        if (instance == null ) {
            instance = new testDemo();
        }
        return instance;
    }
}
