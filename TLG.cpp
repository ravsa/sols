#include <iostream>
using namespace std; 

int main()
{
    ios::sync_with_stdio(false);
    int T, A = 0, B = 0, _max = 0;
    int _A, _B, winner = 1;
    cin >> T;
    while(T--){
        cin >> _A >> _B;
        A += _A;
        B += _B;
        _A = (A - B);
        _B = (B - A);
        if(_A > _max){
            _max = _A;
            winner = 1;
        }
        else if (_B > _max){
            _max = _B;
            winner = 2;
        }
    }
    cout << winner << " " <<_max << endl;
    return 0;
}
