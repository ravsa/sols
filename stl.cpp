#include <iostream>
#include <vector>
#include <algorithm>
#define N 8
using namespace std;
int main()
{
    int array[] = {2, 1, 10, 9, 6, 7, 4, 2};
    int i, j, key;
    for (i = 0; i < N ; ++i){
        key = array[i];
        j = i-1;
        while( j>=0 && (key<array[j])){
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = key;
    }
    for (i = 0; i < N-1; ++i) {
        cout << array[i] << endl;
    }
    
}
