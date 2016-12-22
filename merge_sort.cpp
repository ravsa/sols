#include <iostream>
#define size 8

void combine(int *array, int low, int mid, int high){
    int i = low, j = mid + 1, k = low;
    int temp[size];
    j = mid+1;
    while(i <= mid && j <= high)
        if(array[i]<array[j])
            temp[k++] = array[i++];
        else
            temp[k++] = array[j++];
    while(i<=mid)
        temp[k++] = array[i++];
    while(j<=high)
        temp[k++] = array[j++];
    for(k=low;k<=high;++k)
        array[k] = temp[k];
}
void split(int *array, int low, int high){
    if(low<high){
        int mid = (low+high)/2;
        split(array, low, mid);
        split(array, mid+1, high);
        combine(array, low, mid, high);
    }
}
using namespace std;
int main()
{
    int array[] = {3,2,7,1,3,4,7,0};
    split(array, 0, size-1);
    for (auto i : array ) {
        cout << i << endl;
    }
    return 0;
}
