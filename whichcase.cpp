#include <iostream>
#include <math.h>
using namespace std;
bool fib(int *arr, int size){
    int a = arr[0], b = arr[1];
    for(int i = 2; i<size; i++){
        int c = a + b;
        if (c != arr[i])
            return false;
        a = arr[i-1];
        b = arr[i];
    }
    return  true;
}
bool natural(int *arr, int size){
    for(int i = 0; i < size - 1; i++)
        if ((arr[i+1] - arr[i]) != 1)
            return  false;
    return  true;
}
bool square(int *arr, int size){
    int c = sqrt(arr[0]);
    for(int i = 1;i< size; i++)
        if (sqrt(arr[i]) != ++c)
            return  false;
    return true;
}
void which_case(int *arr, int size){
    if (natural(arr, size))
        std::cout << "case 1" << std::endl;
    if (fib(arr, size))
        std::cout << "case 2" << std::endl;
    if (square(arr, size))
        std::cout << "case 3" << std::endl;
}

int main()
{
    int arr[7] = {4, 9, 16, 25, 36, 49, 64};
    which_case(arr, 7);
    return 0;
}
