#include <iostream>
#include <cstring>
#include <cstdio>
#include <string.h>
using namespace std;
char stack[100];
int top = -1;
void push(char ch){
    stack[++top] = ch;
}
char pop(){
    return stack[top--];
}
char current(){
    if (top == -1)
        return '#';
    return stack[top];
}
bool isempty(){
    return top == -1 ? true : false;
}
int preced(char ch){
    switch(ch){
        case '(': return 1;
        case '+':
        case '-': return 2;
        case '*':
        case '/': return 3;
        case '^': return 4;
        default: return 0;
    }
}
void swap (char &a, char &b){
    char temp = a;
    a = b;
    b = temp;
}
void reverse(char *str){
    char *end = str + strlen(str) - 1;
    while (str < end){
        swap(*str, *end);
        str++;
        end--;
    }
}

void postfix(char *infix){
    char ch;
    while((ch = *infix) != '\0'){
        if (ch == '(')
            push(ch);
        else if (('a' <= ch && ch <= 'z') || ('0' <= ch && ch <= '9'))
            cout << ch ;
        else if (ch == ')'){
            while(current() != '(')
                cout << pop();
            pop();
        }
        else{
            while(preced(ch) <= preced(current()))
                cout << pop();
            push(ch);
        }
        infix += 1;
    }
    while(!isempty())
        cout << pop();
    cout << endl;
}

void prefix(char *infix){
    reverse(infix);
    char pref[100];
    int k = 0;
    char ch;
    while((ch = *infix) != '\0'){
        if (ch == ')')
            push(ch);
        else if (('a' <= ch && ch <= 'z') || ('0' <= ch && ch <= '9'))
            pref[k++]=ch;
        else if (ch == '('){
            while(current() != ')')
                pref[k++] = pop();
            pop();
        }
        else{
            while(preced(ch) <= preced(current()))
                pref[k++] = pop();
            push(ch);
        }
        infix += 1;
    }
    while(!isempty())
        pref[k++] = pop();
    pref[k] = '\0';
    reverse(pref);
    reverse(infix);
    cout << pref<<endl;
}

int main()
{
    char infix[] = "b*c+(d)";
    postfix(infix);
    prefix(infix);
    return 0;
}
