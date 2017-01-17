#include <iostream>
using namespace std;    
int main()
{
    int T;
    float  S, SG, FG, D, Time, other_car_speed, sebi_speed, father_speed;
    cin>>T;
    while(T--){
        cin>>S>>SG>>FG>>D>>Time;
        other_car_speed = (((((D * 50) / 1000)) / Time) * 3600) + S;
        sebi_speed = other_car_speed - SG;
        father_speed = other_car_speed - FG;
        sebi_speed = sebi_speed  < 0 ? ((-1) * sebi_speed ) : sebi_speed; 
        father_speed = father_speed  < 0 ? ((-1) * father_speed ) : father_speed; 
        if (sebi_speed < father_speed)
            cout << "SEBI" << endl;
        else if (sebi_speed > father_speed)
            cout << "FATHER" << endl;
        else
            cout << "DRAW" << endl;
    }
    return 0;
}
