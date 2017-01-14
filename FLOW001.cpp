#include <iostream>
using namespace std; 
int main()
{
    ios::sync_with_stdio(false);
    int N;
    int A, B;
    cin >> N;
    while(N--){
        cin >> A >> B;
        cout << A + B << endl;
    }
    return 0;
}
