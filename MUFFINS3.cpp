#include <iostream>
using namespace std; 
int main()
{
    ios::sync_with_stdio(false);
    int T;
    long long N;
    cin >> T;
    while(T--){
        cin >> N;
        cout << (N/2) + 1 << endl;
    }
    return 0;
}
