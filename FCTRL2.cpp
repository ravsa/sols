#include <iostream>
#define MAX 1000
using namespace std;

void reverse(int *rec, int size){
    int i = 0;
    size--;
    while(i<=size){
        swap(rec[i], rec[size]);
        i++;
        size--;
    }
}

int multiply(int res[], int x, int size){
    int carry = 0;
    int product;
    reverse(res, size);
    for (int i = 0; i <size; ++i) {
        product = res[i] * x + carry;
        res[i] = product % 10;
        carry = product / 10;
    }
    while(carry){
        res[size] = carry%10;
        carry /= 10;
        size++;
    }
    reverse(res, size);
    return size;
}

int main()
{
    int T, num, size;
    ios::sync_with_stdio(false);
    cin >> T;
    while(T--){
        cin >> num;
        int res[1000];
        res[0] = 1;
        size = 1;
        while (num){
            size = multiply(res, num, size);
            num--;
        }
        for (int i = 0; i < size; ++i) {
           cout << res[i];
        }
        cout <<endl;
    }

    return 0;
}
