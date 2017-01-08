#include <iostream>
using namespace std;

int compare(const char *str1, const char *str2){
    while (*str1 &&  (*str2 == *str1 )){
        str1++, str2++;
    }
    return *str1 - *str2;
}
int main()
{
    const char *str1[5] = {"ravi", "raja", "popaya", "tom", "taj"};
    for(int i=0; i<5; i++){
        for(int j=i; j<5; j++){
            if (compare(str1[i], str1[j]) > 0)
            {
                const char *temp = str1[i];
                str1[i] = str1[j];
                str1[j] = temp;
            }
        }
    }
    for (auto i : str1) {
       cout << i << endl; 
    }
    return 0;
}
