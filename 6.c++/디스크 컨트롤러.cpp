#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct boolCheck{
    bool operator()(vector<int> a, vector<int> b){
        return a[1]>b[1];
    }
};
int solution(vector<vector<int>> jobs) {
    priority_queue<vector<int>,vector<vector<int>>,boolCheck> heaps;
    sort(jobs.begin(),jobs.end());
    int josbSize = jobs.size();
    int t  = jobs[0][0];
    int answer = 0;
    int totalTime = 0;
    int i = 0;
    while(i<josbSize){
        while(i<josbSize and t>=jobs[i][0]) {
          heaps.push(jobs[i]);
          i++;
        }
        if(i<josbSize and heaps.empty()) t=jobs[i][0];
        if(!heaps.empty()){
            totalTime += t-heaps.top()[0];
            totalTime += heaps.top()[1];
            t+=heaps.top()[1];
            heaps.pop();
        }
    }
    while(!heaps.empty()){
        totalTime += t-heaps.top()[0];
        totalTime += heaps.top()[1];
        t+=heaps.top()[1];
        heaps.pop();        
    }
    totalTime /=josbSize;
    return totalTime;
}