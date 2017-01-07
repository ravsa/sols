#include <iostream>
#include <queue>
using namespace std; 
struct node{
    int data;
    node *right;
    node *left;
};

node *insert(node *tree, int num){
    if (tree == NULL){
        node *temp;
        temp = new node;
        temp->left = temp->right = NULL;
        temp->data = num;
        return temp;
    }
    else{
        if (tree->data > num)
            tree->left = insert(tree->left, num);
        else if (tree->data < num)
            tree->right = insert(tree->right, num);
        else 
            cout << "Duplicate Element: " << num << endl;
    }
    return tree;
}

void inorder(node *tree){
    if (tree){
        inorder(tree->left);
        cout << tree->data << endl;
        inorder(tree->right);
    }
}

void preorder(node *tree){
    if (tree){
        cout << tree->data << endl;
        preorder(tree->left);
        preorder(tree->right);
    }
}

void postorder(node *tree){
    if (tree){
        postorder(tree->left);
        postorder(tree->right);
        cout << tree->data << endl;
    }
}

bool search(node *tree, int element){
    if(tree==NULL)
        return false;
    else if (tree->data == element)
        return true;
    else if (tree->data > element)
        return search(tree->left, element);
    else
        return search(tree->right, element);
}

int min(node *tree){
    if(tree){
        if(tree->left)
            return min(tree->left);
        return tree->data;
    }
    return 0;
}

int max(node *tree){
    if(tree){
        if(tree->right)
            return max(tree->right);
        return tree->data;
    }
    return 0;
}

void free_(node *tree){
    if (tree){
        free_(tree->left);
        free_(tree->right);
        delete tree;
    }
}

node* Delete(node* root, int data){
    if (!root) return root;
    else if(data < root->data) root->left = Delete(root->left, data);
    else if(data > root->data) root->right = Delete(root->right, data);
    else{
        //case 1: No Child
        if(root->left == NULL && root->right == NULL){
            delete root;
            root = NULL;
        }
        //case 2: One child
        else if (root->left == NULL){
            node *temp = root;
            root = root->right;
            delete temp;
        }
        else if (root->right == NULL){
            node *temp = root;
            root = root->left;
            delete temp;
        }
        //case 3: two child
        else{
            root->data = min(root->right);
            root->right = Delete(root->right, root->data);
        }
    }
    return root;
}

int main()
{
    node *tree = NULL;
    tree = insert(tree, 7);
    tree = insert(tree, 2);
    tree = insert(tree, 6);
    tree = insert(tree, 5);
    tree = insert(tree, 4);
    tree = insert(tree, 1);
    tree = insert(tree, 9);
    tree = insert(tree, 8);
    tree = insert(tree, 10);
    preorder(tree);
    Delete(tree, 2);

    cout << "******************************************" << endl;
    cout << "              AFTER DELETION " << endl;
    cout << "******************************************" << endl;

    preorder(tree);
    free_(tree);
    return 0;
}
