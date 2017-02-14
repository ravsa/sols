#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int c,x,m,t;
	cin>>c>>m>>t;
	while(t>0)
	{
		cin>>x;
		long long int a[x+1],sum=0,i,j;
		a[0]=0;
		a[1]=a[2]=1;
		for(i=3;i<=x;i++)
		{
			a[i]=c*a[i-1]+a[i-2];
			sum=sum+a[i];
		}
		if(x==1)
			cout<<"1"<<endl;
		else if(x==2)
			cout<<"2"<<endl;
		else
			cout<<(sum+2)%m<<endl;
		t--;
	}
}

