#include <iostream>
using namespace std; 
int partition(int *array, int left, int right){
    int mid = (left + right)/2;
    int pivot = array[mid];
    swap(array[mid], array[left]);
    int i = left + 1;
    int j = right;
    while(i<=j){
        while(i<=j && array[i] <= pivot)
            i++;
        while(i<=j && array[j] > pivot)
            j--;
        if (i<j)
            swap(array[i], array[j]);
    }
    swap(array[left], array[i-1]);
    return i - 1;
}

void quick_sort(int *array, int left, int right){
    if (left<right){
        int part = partition(array, left, right);
        quick_sort(array, left, part-1);
        quick_sort(array, part+1, right);
    }
}
int main()
{
    int array[] = {9,1,8,2,7,3,7,4,6,5};
    int size = 9;
    quick_sort(array, 0, size);
    for (int i = 0; i <=size ; ++i) {
        cout << array[i] << endl;
    }
    return 0;
}
