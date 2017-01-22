#include <stdio.h>
int *func();
int main()
{
    auto int *x;
    int *(*ptr)();
    ptr = &func;
    x = (*ptr)();
    printf("%d\n", *x);
    return 0;
}
int *func(){
    static int a = 10;
    return &a;
}
