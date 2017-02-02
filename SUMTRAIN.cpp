#include <iostream>
using namespace std; 
int main()
{
    ios::sync_with_stdio(false);
    int t, n, a[100][100];
    cin >> t;
    while(t--){
        cin >> n;
        for (int i = 0; i < n; ++i) 
            for (int j = 0; j <= i; ++j)
                cin>>a[i][j];
        for (int i = n-1 ; i > 0 ; --i ) 
           for (int j = 0; j < n; ++j) 
               if(a[i][j]>a[i][j+1])
                    a[i-1][j] = a[i-1][j] + a[i][j];
               else
                   a[i-1][j] = a[i-1][j] + a[i][j+1];
        cout << a[0][0] << endl;
    }
    return 0;
}
