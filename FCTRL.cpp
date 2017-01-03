#include <iostream>
using namespace std; 
int main()
{
    int N, num, temp;
    ios::sync_with_stdio(false);
    cin >> N;
    for (int i = 0; i < N; ++i) {
        int zeros = 0, five = 5;
        cin >> num;
        while((temp = num / five)){
            zeros = zeros + temp;
            five *= 5;
        }
        cout << zeros << endl;
    }
    return 0;
}
