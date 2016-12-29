#include <iostream>
#include <climits>
#define MAX 5
using namespace std; 

struct node{
    int info;
    node *next;
};
class link
{
    node *create_node(int value){
        node *temp = new(struct node);
        temp->info = value;
        temp->next = NULL;
        return temp;
    };
    public:
    node *root;
    node *last;
    link(){root = NULL;
        last = NULL;}
    ~link();
    void add_front(int value);
    void add_rear(int value);
    int delete_front();
    int delete_rear();
    void display();
};

void link::add_rear(int value){
    node *temp = create_node(value);
    if(!root){
        root = temp;
        last = temp;
    }
    else{
        last->next = temp;
        last = temp;
    }
}

void link::add_front(int value){
    node *temp = create_node(value);
    if(!root){
        root = temp;
        last = temp;
    }
    else{
        temp->next = root;
        root = temp;
    }
}

int link::delete_rear(){
    node *temp = root;
    node *p = NULL;
    if(!root) return INT_MAX;
    while(temp->next){
        p = temp;
        temp = temp->next;
    }
    int value = temp->info;
    if (p!=NULL)
        p->next = NULL;
    else
        root = NULL;
    last = p;
    delete temp;
    return value;
}
int link::delete_front(){
    if(!root) return INT_MAX;
    int value = root->info;
    node *temp = root;
    root = root->next;
    if (!root) last = NULL;
    delete temp;
    return value;
}
void link::display(){
    node *temp = root;
    while(temp){
        cout <<"[" <<temp->info << "]-";
        temp = temp->next;
    }
    cout <<endl;
}
link::~link(){
    node *temp = root;
    node *p = root;
    while(p){
        p = p->next;
        delete temp;
        temp = p;
    }
}

class queue{
    link Q;
    public:
    void push(int value){Q.add_rear(value);};
    int pop(){return Q.delete_front();};
    int top(){return (Q.last)->info;};
    bool isEmpty(){return Q.last ? false : true; };
    void display(){ Q.display(); }
};

int cqueue[MAX];
int front = -1;
int rear = -1;
int count = 0;

void push(int value){
    if (!~front){
        front = 0;
    }
    if (count < MAX){
    rear = (rear + 1) % MAX;
    cqueue[rear] = value;
    count++;
    }
    else{
        cout <<"queue overflow"  << endl;
    }
}
int pop(){
    if(count>0){
        int temp = cqueue[front];
        front = (front+1) % MAX;
        count--;
        return temp;
    }
    cout<<"underflow"<<endl;
    return INT_MAX;
}
void display(){
    for(auto &i: cqueue)
        cout << i << endl;
}
int main()
{
    push(1);
    push(2);
    push(3);
    push(5);
    push(6);
    display();
    return EXIT_SUCCESS;
}
