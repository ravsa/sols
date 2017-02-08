#include <iostream>
using namespace std; 
int main()
{
    ios::sync_with_stdio(false);
    int T, d;
    int array[1000001] = {0};
    cin>>T;
    for (int i = 0; i < T; ++i){
        cin >> d;
        array[d]++;
    }
    for (int i=0;i<1000001;++i) {
        while(array[i]){
            cout << i << endl;
            array[i]--;
        }
    }
    return 0;
}
