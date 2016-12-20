#include <stdio.h>
long int  gcd(  long int a,  long int b){
    if (b==0) return a;
    return gcd(b, a%b);
}

long int  lcm(  long int  a,   long int  b){
    a = (a > 0)?a:-1*a;
    b = (b > 0)?b:-1*b;
    return (a*b / gcd(a,b));
}

void testcase(  long int *arr,  long int k,  long int size){
    long int lcmk = lcm(arr[0], arr[1]);
    for (  long int i = 0; i < size; ++i)
        lcmk = lcm(lcmk, arr[i]);
    printf("%s",(((lcmk % k) == 0)?"YES":"NO"));
}
int  main()
{
    long int T, N, K;
    scanf("%ld",&T);
    scanf("%ld %ld",&N, &K);
    long int arr[N];
    for (long int i = 0; i < N; ++i)
        scanf("%ld",&arr[i]);
    testcase(arr,K,N);
    return 0;
}
