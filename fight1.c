#include <stdio.h>
int main()
{
    int T;
    scanf("%d", &T);
    while (T--){
        char arr[100001];
        int count = 0, max = 0, i;
        scanf("%s",arr);
        for(i = 0; arr[i] != '\0'; i++){
            if (arr[i] == '1')
                count++;
            else{
                if (count > max)
                    max = count;
                count = 0;
            }
        }
    if (count > max)
        max = count;
    printf("%d\n", max);
    }
    return 0;
}
