#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer(2);
    set<string> gemsSet;
    map<string,int> mapGems;
    for(int i=0;i<gems.size();i++) gemsSet.insert(gems[i]);
    
    int gemSu = gemsSet.size();
    int gemSuNow = 0;
    int start = 0;
    int gugan = -1;
    queue<string> qu;
    for(int i=0;i<gems.size();i++){
        qu.push(gems[i]);
        mapGems[gems[i]]++;
        if(mapGems[gems[i]]==1) {
            gemSuNow++;
            if(gemSuNow==gemSu) {
                answer[0] = start;
                answer[1] = i;
                gugan = answer[1]-start;
            }
        }
        while(mapGems[qu.front()]>1){
            mapGems[qu.front()]--;
            qu.pop();
            start++;
            if(gugan!=-1 and i-start<gugan){
                answer[0]= start;
                answer[1]= i;
                gugan=i-start;
            }
        }
    }
    
    answer[0]++;
    answer[1]++;
    return answer;
}