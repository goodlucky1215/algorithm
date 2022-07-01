#include <string>
#include <vector>
#include <iostream>
using namespace std;


long long answer = 0;
void plusOrMinus(vector<vector<int>>& su,vector<long long>& aLong,int par,int chi){
    for(int i=0;i<su[chi].size();i++){
        if(su[chi][i]!=par) plusOrMinus(su,aLong,chi,su[chi][i]);
    }
    answer+= abs(aLong[chi]);
    aLong[par]+= aLong[chi];
}

long long solution(vector<int> a, vector<vector<int>> edges) {
    vector<long long> aLong;
    vector<vector<int>> su(300001);
    for(int i:a)aLong.push_back(i);
    for(vector<int> v:edges){
        su[v[0]].push_back(v[1]);
        su[v[1]].push_back(v[0]);
    }
    plusOrMinus(su,aLong,0,0);
    if(aLong[0]==0) return answer;
    else return -1;
}