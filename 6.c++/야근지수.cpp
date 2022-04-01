#include <string>
#include <vector>
#include <queue>
using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    priority_queue<int> pq;
    for(int i:works){
        pq.push(i);
    }
    for(int i=0;i<n;i++){
        int p =pq.top();
        if(p==0) return 0;
        pq.pop();
        pq.push(--p);
    }
    while(!pq.empty()){
        answer+= pq.top()*pq.top();
        pq.pop();
    }
    return answer;
}