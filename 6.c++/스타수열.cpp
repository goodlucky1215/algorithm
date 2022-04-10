#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
using namespace std;

int solution(std::vector<int> a) {
    int aLen = a.size();
    map<int,int> ma;
    for(int i=0;i<aLen;i++){
        ma[a[i]]++;
    }
    
    int answer = 0;
    for(auto it : ma){
        if(answer>=it.second*2) continue;
        int re = 0;
        for(int j=0;j<aLen-1;j++){
            if(a[j]!=it.first and a[j+1]!=it.first) continue;
            if(a[j]==a[j+1]) continue;
            re++;
            j++;
        }
        answer = max(answer,re*2);
        
    }

    return answer;
}