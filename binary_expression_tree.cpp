#include <iostream>
#include <stack>
using namespace std;

struct et
{
    char value;
    et *right;
    et *left;
};
bool isopertor(char ch){
    if (ch == '+' || ch == '-' || ch == '/' || ch == '*' || ch == '^')
        return true;
    return false;
}
et* create_node(char v){
    et *temp = new et;
    temp->left = NULL;
    temp->right = NULL;
    temp->value = v;
    return temp;
}

void inorder(et *t){
    if(t){
        inorder(t->left);
        cout<<t->value;
        inorder(t->right);
    }
}
et* construct_tree(char infix[]){
    et *t, *t1, *t2;
    char ch;
    std::stack<et*> st ;
    while((ch=*infix)!='\0'){
        if(!isopertor(ch))
        {
            t = create_node(ch);
            st.push(t);
        }
        else{
            t = create_node(ch);
            t1 = st.top();
            st.pop();
            t2 = st.top();
            st.pop();
            t->right = t1;
            t->left = t2;
            st.push(t);
        }
        infix++;
    }
    t = st.top();
    st.pop();
    return t;
}

int main()
{
    // char infix[] = "a*b";
	char postfix[] = "ab+ef*g*-";
    et *root = construct_tree(postfix);
    inorder(root);
    return 0;
}
