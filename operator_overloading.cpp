#include <iostream>
using namespace std; 
namespace net {
int abs (int value){
    cout << "int called" << endl;
    return value<0 ? value*-1 : value;
}
double abs (double value){
    cout << "double is called" << endl;
    return value<0 ? value*-1 : value;
}
long abs (long value){
    cout << "long is called" << endl;
    return value<0 ? value*-1 : value;
}
}
int main()
{
    cout << net::abs((int)100L + 1) << endl;
    return 0;
}
