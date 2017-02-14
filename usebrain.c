#include <stdio.h>
int main(){
    int i, num, j;
    for(i=0;i<7;i++){
        scanf("%d", &num);
        int count = 0;
        for(j=1;j<=num;j++){
            if (num % j==0)
                count++;
        }
        printf("%d ", count);
    }
    return  0;
}
