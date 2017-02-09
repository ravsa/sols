#include <iostream>
#include <cstring>
#include <sstream>
using namespace std; 

class red{
    int i;
    public:
    void set_i(int x){i=x;};
    int get_i(){return i;};
};

class blue:public red{
    int j;
    public:
    void set_j(int x){j=x;};
    int get_j(){return j;};
};

int main()
{
    red *r;
    blue b;
    r = &b;
    r->set_i(4);
    ((blue*)r)->set_j(2);
    cout << ((blue*)r)->get_j()<< endl;
    return 0;
}
