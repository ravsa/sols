#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int X;
    float balance;
    cin>>X;
    cin>>balance;
    cout << fixed << setprecision(2);
    if (X % 5 != 0 || (float)X+0.50 > balance)
        cout <<  balance <<endl;
    else
        cout <<(balance - ((float)X+0.50)) << endl;
    return 0;
}
