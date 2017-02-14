#define DOIT {printf("no\n");continue;}
#include<iostream>
#include<stdio.h>
using namespace std;
#define ll long long
ll take ()
{
	ll a=0;
	char temp;
	while (1)
	{
		temp=getchar_unlocked();
		if (temp>='0'&&temp<='9') break;
	}
	a=temp-'0';
	while (1)
	{
		temp=getchar_unlocked()-'0';
		if (temp<0||temp>9) return a;
		a=a*10+temp;
	}
}

int main()
{
	ll t=take(),c,d,l;
	while(t--){
		c=4*take();d=4*take();l=take();
		if(l%4) DOIT
		l-=d;
		if(l<0) DOIT
		if(l<(c-2*d)||l>c) DOIT
		printf("yes\n");
	}
}
