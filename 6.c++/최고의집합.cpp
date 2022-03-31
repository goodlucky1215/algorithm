#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    if(n>s) return {-1};
    vector<int> answer(n,s/n);
    int namugi = s%n;
    for(int i =n-1;namugi>0;i--,namugi--) answer[i]+=1;
    return answer;
}