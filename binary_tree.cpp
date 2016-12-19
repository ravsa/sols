#include <iostream>
#include <cstdlib>
using namespace std; 
struct node {
    int data;
    node *right;
    node *left;
};

static int count = 1;
node* create_node(int value, node *tree){
    if (tree == NULL){
        tree = new(struct node);
        tree->data = value;
        tree->left = tree->right = NULL;
        count++;
    }
    else if(value < tree->data)
        tree->left = create_node(value, tree->left);
    else
        tree->right = create_node(value, tree->right);
    return tree;
}
void freex(node *tree){
    if(tree){
        freex(tree->left);
        freex(tree->right);
        delete tree;
    } }
void trav(node *tree){
    if(tree){
        trav(tree->left);
        cout << "["<<tree->data <<"] ";
        trav(tree->right);
    }
}
int main()
{
    node *root = NULL;
    int a[] = { 15, 4, 7, 1, 2, 8, 9, 16, 18, 37, 89, 11, 21, 26, 3, 77 };
    for (auto i: a)root = create_node(i, root);
    trav(root);
    freex(root);
    return 0;
}
