#include <iostream>
#include <cstring>
#include <cstdio>
#include <climits>

using namespace std;
/**********Utility Functions************/
// display sorted array
void disp(const int *array, const int size)
{
    for (int i = 0; i < size ; ++i) 
        cout << array[i] << endl;  
}
//swaping two elements
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}
//create copy of array
void copy(int *array,int *duplicate, int size){
    for (int i = 0; i <size ; ++i) {
        duplicate[i] = array[i]; 
    }
}

/**********Sorting Algos************/
//bubble sort O(n^2)
void bubble_sort(int *array, const int size){
    int i,j;
    for (i = 0; i < size - 1; ++i)
        for(j = 0; j < size-i-1; ++j)
            if(array[j]>array[j+1])
                swap(array[j],array[j+1]);
}

//insertion sort O(n^2)
void insertion_sort(int *array, const int size)
{
    int i,j,key;
    for (i = 0; i < size; ++i) {
        key = array[i];
        j = i-1;
        while((j>=0) && (key<array[j])){
            array[j+1] = array[j]; 
            j--; 
        }
        array[j+1] = key; }
}

//selection sort O(n^2)
void selection_sort(int *array, const int size){
    int i,j, min;
    for (i = 0; i < size-1 ; ++i) {
        min = i;
        for (j = i+1; j < size ; ++j) {
            if(array[j]<array[min])
                min = j;
        }
        swap(array[i], array[min]);
    }
}

//quicksort sort O(n*logn) -> O(n^2)
int partition(int *array, const int left, const int right){
    const int mid = left + (right - left)/2;
    // const int mid = (left+right)/2;
    const int pivot = array[mid];
    swap(array[left], array[mid]);
    int i = left + 1;
    int j = right;
    while(i<=j){
        while(i <= j && array[i] <= pivot){
            i++;
        }
        while(i <= j && array[j] > pivot) {
            j--;
        }
        if (i < j) {
            swap(array[i], array[j]);
        }
    }
    swap(array[i - 1],array[left]);
    return i - 1;
}

void quick_sort(int *array, const int left, const int right){
    if(left>=right){
        return;
    }
    int part = partition(array, left, right);
    quick_sort(array, left, part-1);
    quick_sort(array, part+1, right);
}

//merge sort O(n*logn)

void combine(int *array, int low, int mid, int high, int size){

    int i, j, k;
    int temp[size];
    k = low;
    i = low;
    j = mid+1;
    while(i <= mid && j <= high){
        if(array[i] <= array[j]){
            temp[k] = array[i];
            i++;
            k++;
        }
        else{
            temp[k] = array[j];
            j++;
            k++;
        }
    }

    while(i<=mid){
        temp[k] = array[i];
        i++;
        k++;
    }

    while(j<=high){
        temp[k] = array[j];
        j++;
        k++;
    }

    for(k=low; k<=high; ++k){
        array[k] = temp[k];
    }
}

void merge_sort(int *array, const int low, const int high, int size){
    if(low<high){
        int mid = (low+high)/2;
        merge_sort(array, low, mid, size);
        merge_sort(array, mid+1, high, size);
        combine(array,low,mid,high,size );
    }
}

//radix sort
void radix_sort(int *array, int size){
    int max = INT_MIN;
    int total_no = 0;
    for (int i = 0; i < size ; ++i)
        if(max<array[i])
            max = array[i];
    while(max){
        total_no++;
        max /= 10;
    }
    cout << total_no << endl;
}
int main()
{
    int array[] = {9,1,8,2,7,3,6,4,5};

    quick_sort(array, 0, 8);
    for (int i = 0; i < 9 ; ++i) {
        cout << array[i] << endl;
    }
}
