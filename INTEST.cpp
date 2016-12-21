#include <iostream>
using namespace std;
int main()
{
    int n, k;
    int temp;
    ios::sync_with_stdio(false);
    cin >>n>>k;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        cin>>temp;
        if ((temp % k) == 0)
            count++;
    }
    cout << count << endl;
    return 0;
}
