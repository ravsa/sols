#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    ios::sync_with_stdio(false);
    std::cin >> t;
    while(t--)
    {
        int n,k,tmp;
        std::cin >> n >> k;
        list<int> v;
        list<int> :: iterator it;
        for(int i=0;i<n;++i)
        {
            std::cin >> tmp;
            v.push_back(tmp);
        }
        for(it=v.begin();it!=v.end();)
        {
            int tmp1=*(v.begin());
            if(k==0)
                break;
            int val=*it;
            it++;
            int val1=*it;
            if(val>=val1)
                continue;
            else
            {
                --it;
                v.erase(it);
                int tmp2=*it;
                if(tmp1!=tmp2)
                    --it;
                else
                    it=v.begin();
                k--;
            }
        }
        if(k!=0)
        {
            for(int i=0;i<k;++i)
                v.pop_back();
        }
        for(it=v.begin();it!=v.end();++it)
            std::cout << *it;
        std::cout << std::endl;
    }
    return 0;
}
