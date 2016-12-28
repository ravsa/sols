#include <iostream>
using namespace std; 
struct node {
    int coff;
    int expo;
    node *next;
};

void freex(node **root){
    node *temp = *root;
    while(*root){
        *root = (*root)->next;
        delete temp;
        temp = *root;
    }
}

node *create(int coff, int expo){
    node *temp = new node;
    temp->coff = coff;
    temp->expo = expo;
    temp->next = NULL;
    return temp;
}

void insert_(node **root,node **current_node, int coff, int expo){
    node *temp = create(coff, expo);
    if(*root == NULL){
        *root = temp;
        *current_node = temp;
    }
    else{
        (*current_node)->next = temp;
        *current_node = temp;
    }
}

void display(const char *str = "", node *root = NULL){
    node *temp = root;
    cout << str << endl;
    while(temp){
        cout<<temp->coff;
        if(temp->expo){
            cout<<"X";
            if(temp->expo != 1) cout<<"^"<< temp->expo;
        }
        if (temp->next) if (temp->next->coff > 0) cout<<"+";
        temp = temp->next;
    }
    cout << endl;
}

void add(node *a, node *b){
    node *result = NULL;
    node *temp, *last;
    while(a && b){
        if (a->expo > b->expo){
            temp = create(a->coff, a->expo);
            a = a->next;
        }
        else if ( b->expo > a->expo ){
            temp = create(b->coff, b->expo);
            b = b->next;
        }
        else{
            if ((a->coff + b->coff) != 0)
                temp = create((a->coff+b->coff), a->expo);
            a = a->next;
            b = b->next;
        }
        if(!result){
            result = temp;
            last = temp;
        }
        else {
            last->next = temp;
            last = temp;
        }
    }
    for(;a;a=a->next){
        temp = create(a->coff,a->expo);
        if(!result){
            result = temp;
            last = temp;
        }
        else {
            last->next = temp;
            last = temp;
        }
    }
    for(;b;b=b->next){
        temp = create(b->coff,b->expo);
        if(!result){
            result = temp;
            last = temp;
        }
        else {
            last->next = temp;
            last = temp;
        }
    }
    last->next = NULL;
    display("addition of polynomials", result);
    freex(&result);
}
void merge(node *eq1, node *eq2){
    while(eq1->next) eq1 = eq1->next;
    eq1->next = eq2;
}

int main()
{
    freopen("input.txt", "r", stdin);
    node *eq1 = NULL;
    node *eq2 = NULL;
    node *eq1_temp = NULL;
    node *eq2_temp = NULL;
    int a,p;
    for (int i = 0; i < 4; ++i) {
        scanf("%d %d",&a,&p);
        insert_(&eq1, &eq1_temp, a, p);
    }
    for (int i = 0; i < 4; ++i) {
        scanf("%d %d",&a,&p);
        insert_(&eq2, &eq2_temp, a, p);
    }
    display("eqution 1", eq1);
    display("eqution 2", eq2);
    add(eq1, eq2);
    merge(eq1, eq2);
    display("merged eqution 1 and 2", eq1);
    freex(&eq1);
    // freex(&eq2);
    return 0;
}
