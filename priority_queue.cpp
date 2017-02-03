#include <iostream>
#define MAX 10
using namespace std;    
struct queue  {
    int rear, front;
    int item[MAX];
};
int remove(queue *qptr){
    int smallest, f, loc, i;
    f = qptr->front;
    if(qptr->front == qptr->rear){
        cout << "UnderFlow" << endl;
        return EXIT_FAILURE;
    }
}

int main()
{
    return EXIT_SUCCESS;
}
