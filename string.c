#include<stdio.h>
#include<string.h>
int con[26];
void init(){
    for(int i=0;i<26;i++)
        con[i] = 0;
}
int main(int argc, char *argv[])
{
    /** freopen("input.txt", "r", stdin); */
    int i = 0;
    int flag = 1;
    init();
    /** scanf("%s",str); */
    for(i=0;argv[1][i]!='\0';i++)
        con[argv[1][i]-97]++;
    for(i=0;i<26;i++)
        if((con[i]&1)!=0)
            flag = 0;
    if(flag)
        printf("YES");
    else
        printf("NO");
    return 0;
}
