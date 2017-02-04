#include <iostream>
#include <numeric>
#include <bits/stdc++.h>
using namespace std; 
int func(int value){
    return ( value * (value+1) / 2);
}
int main()
{
    freopen("input.txt","r",stdin);
    int a[100], p[100];
    int n = 100;
    for (int i = 0; i < n; ++i) scanf("%d", &a[i]), p[i] = i;
    sort(p, p+n, [=](int i, int j) { return a[i] < a[j]; });
    return 0;
}
