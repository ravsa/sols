#include <iostream>
using namespace std;
void t(int n){
    if (n/2){
        cout << n << endl;
        t(n/2);
    };
    cout<<(n%2);
}
int main()
{
    t(10);
    return 0;
}
