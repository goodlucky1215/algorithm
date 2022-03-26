#include <iostream>
#include <vector>
using namespace std;

int solution(int n, vector<int> stations, int w)
{
int answer = 0;
int w2 =w*2+1;
int start = 0;
int i = 0;
int stationsSize = stations.size();
int end = stations[i]-w;

while(true){
 while(start+1>=end){
 start = max(stations[i]+w, start);
 i++;
 if(i<stationsSize) end = stations[i]-w;
 else {
     end = n+1;
     break;
     }
}
if(n<=start) break;
answer++;
start+=w2;
}
return answer;
}