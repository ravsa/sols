#include <iostream>
#include <limits.h>
typedef unsigned long long ll;
using namespace std; 
ll gcd(ll a, ll b){
    if (b == 0) return a;
    return gcd(b, a%b);
}
ll lcm(ll a, ll b){
    return (a*b / (gcd(a, b)));
}
int main()
{
    int T, N, i, j;
    cin >> T;
    while(T--){
        cin >> N ;
        ll A[N], min=LONG_MAX;
        for (i = 0; i < N; ++i)
            cin >> A[i];
        for (i = 0; i < N; ++i)
            for (j = i + 1; j < N; ++j){
                ll _lcm = lcm(A[i], A[j]);
                min = min>_lcm ? _lcm : min;
            }
        cout<<min<<endl;
    }
    return 0;
}
