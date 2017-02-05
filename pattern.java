public class pattern {
    public static void main(String[] args) {
        int i,j,n=6 ;
        for (i=1; i<=2*n; i++) {
            if (i<=n) {
                for (j=1;j<=i; j++) {
                    System.out.print(i);
                }
            }
            System.out.println();
            if (i>=n) {
                for (j=2*n-i;j>=1; j--) {
                    System.out.print(2*n-i);
                }
            }
        }
    }
}
