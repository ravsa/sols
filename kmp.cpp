#include <iostream>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <cstdio>

using namespace std;
void  prefix(char * pat, int table[]){
    long M =strlen(pat);
    int len=0, i=1; // longest prefix-suffix length
    table[0] = 0; // prefix table
    while(i < M) {
        if(pat[i] == pat[len]){ // if char matches with previous char increamented;
            len++;
            table[i] = len;
            i++;
        }
        else{
            if(len!=0){
                len = table[len-1]; // if char doesn't match and len is not zero
            }
            else{
                table[i] = 0; 
                i++;
            }
        }
    }
}

void kmp(char * text, char * pat){
    long m = strlen(pat);
    long n = strlen(text);
    int *table = new int[m];
    prefix(pat, table);
    int i = 0;
    int k = 0;
    while (i<n) {
        if(pat[k] == text[i]){ // if char matches increament pattern's k variable and text's i variable
            k++;
            i++;
        }
        if(k==m){
            cout << "pattern is found at "<<i-m << endl;
            k = table[k-1]; //shift from prefix table
        }
        else if(i < n && pat[k] != text[i]){
            if(k!=0)
                k = table[k-1]; //shift from prefix table
            else
                i++;
        }
    }
    delete[] table;
}

int main()
{
    char text[] = "helloworld";
    char pat[] = "lo";
    kmp(text, pat);
    return 0;
}
