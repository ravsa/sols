#include <iostream>

int binary(int[], int, int, int);

int main()
{
    int arr[] = {1,12,13,14,15,21,23,27,34,35,39,42,45,48,50,56,67,78 };
    int key = 23;
int found = binary(arr, key, 0, 18);
    if (found)
        std::cout << "Found at position " <<found << std::endl;
    else 
        std::cout << "Not Found!" << std::endl;
    return 0;
}

int  binary(int arr[], int key , int low, int high)
{
    int mid = (high + low) / 2;
    if (arr[mid] == key)
        return mid + 1;
    if (high < low)
        return 0;
    return (arr[mid]<key? binary(arr,key,mid + 1,high) : binary(arr,key,low,mid-1));
}
