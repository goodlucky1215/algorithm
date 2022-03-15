#include <iostream>
#include <string>
using namespace std;

int pall(string s, int x,int y){
    int t = 1;
    for(int left = x,right = y;left>=0;left--,right++){
        if(s[left]!=s[right]) break;
        t+=2;
    }
    return t;
}
int solution(string s)
{
    int answer = 1;
    int sSize = s.size();
    for(int i = 1;i<sSize;i++){
        answer = max(answer, pall(s,i-1,i+1));
        if(s[i-1]==s[i]) answer = max(answer, pall(s,i-2,i+1)+1);
    }
    return answer;
}