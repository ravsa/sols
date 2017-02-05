#include <iostream>
typedef unsigned long long int  lli;
using namespace std; 
lli NUMBER1[100];
void swap(lli  *a, lli  *b){
    lli  temp = *a;
    *a = *b;
    *b = temp;
}
void reverse(lli  *num, lli  end){
    lli  start = 0;
    end--;
    while(start<=end){
        swap(&num[start], &num[end]);
        start++;
        end--;
    }
}
lli  multiply(lli  *number, lli  multipler, lli  size){
    lli  carry = 0;
    lli  product;
    reverse(number, size);
    for (lli  i = 0; i < size ; ++i) {
        product = number[i] * multipler + carry;
        number[i] = product % 10;
        carry = product/10;
    }
    while(carry){
        number[size] = carry % 10;
        carry /= 10;
        size++;
    }
    reverse(number, size);
    return size;
}
int  main()
{
    lli  a[100] = {1, 2, 3, 4};
    lli  s = multiply(a, 1239230892138012933, 4);
    for (lli  i = 0; i < s; ++i) {
        cout << a[i];
    }
    return 0;
}
