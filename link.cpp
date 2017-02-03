#include <iostream>
#include <cstdio>

using namespace std;
struct node{
    int data;
    node *next;
}; 
node *root = NULL;

void display(){
    node *new_node;
    new_node = root;
    while(new_node!=NULL){
        cout <<"["<<new_node->data<<"]"<< "->";
        new_node =new_node->next;
    }
    cout << "NULL" << endl;
}
bool palindrom(node *tail){
    static node *head = root;
    if(tail){
    if(!palindrom(tail->next)) return false;
    if(head->data != tail->data) return false;
    head = head->next;
    }
    return true;
}
void sorting(){
    node *temp;
    node *p ;
    node *min;
    for (temp=root; temp;temp=temp->next) {
        min = temp;
        for (p=temp->next;p;p=p->next)
            if(min->data<p->data)
                min = p;
        swap(min->data, temp->data);
    }
}
void reverse(){
    node *current = root;
    node *prev = NULL;
    node *next;
    while(current){
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    root = prev;
}

void reverse_(node *right, int j){
    static node* left = root;
    static int i = 0;
    if(right){
        reverse_(right->next, j+1);
        j--;
        i++;
        if(i <= j){
            swap(left->data, right->data) ;
            left = left->next;
        }
        else
            return;
    }
}

int main()
{
    int arr[] = {4, 5, 7, 4, 7, 5, 3};
    int size = 7;
    int i = 0;
    root = new(struct node);
    node *new_node = root ;
    new_node->data=arr[i++];
    while(size>(i++)){
            new_node->next = new(struct node);
            new_node = new_node->next;
            new_node->data=arr[i-1];
    }
    new_node->next = NULL;
    reverse();
    display();
    return 0;
}

