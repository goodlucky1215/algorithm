#include <string>
#include <vector>
#include <algorithm>
using namespace std;

long long solution(int n, vector<int> times) {
    long long timesSize = times.size();
    sort(times.begin(), times.end());
    long long start = 1;
    long long end = (long long)times[timesSize-1]*n;
    long long answer = end;
    while(start<=end){
        long long midTimes =(start+end)/2;
        long long people = 0;
        for(long long i=0;i<timesSize;i++){
            people += (long long) midTimes/times[i];
        }
        if(people>=n) {
            answer = min(answer,midTimes);
            end = midTimes-1;
        }else{
            start = midTimes+1;
        }
        
    }
    return answer;
}