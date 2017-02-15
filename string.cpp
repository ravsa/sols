#include <iostream>
static int alpha[27];
void replace(char *str1, char *str2){
    while(*str2){
        alpha[(int)*str2 - 'A']++;
        str2++;
    }
    while(*str1){
        if (alpha[(int)*str1 - 'A'] != 0)
            *str1 = '+';
        str1++;
    }
}
int main()
{
    char str1[100], str2[100];
    std::cin >> str1 >>str2;
    replace(str1,str2);
    std::cout << str1 << std::endl;
    return 0;
}
