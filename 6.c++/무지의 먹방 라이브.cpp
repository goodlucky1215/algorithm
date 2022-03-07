#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> food_times, long long k) {
    // 음식 갯수와 음식이 제일 적은것부터 담는다.
    int foodSu = food_times.size();
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> qu;
    for(int i=0;i<foodSu;i++){
        qu.push(make_pair(food_times[i],i));
    }
    
    // 제일 작은 수부터 곱해서 시간 만큼 빼준다.
    int foodTimeAll = 0;
    int q = qu.top().first;

    while(k>=foodSu) {
        if(k>=(long long)q*foodSu) { //최소가 더 큰 경우
            foodTimeAll = qu.top().first;
            k-=(long long)q*foodSu;
        }else{
            int t = k/foodSu;
            k-=(long long)t*foodSu;
            foodTimeAll+=t;   
        }
        while(!qu.empty() and qu.top().first<=foodTimeAll){
            food_times[qu.top().second] = 0;
            qu.pop();
            foodSu--;
        }
        if(qu.empty()) return -1;
        q = qu.top().first-foodTimeAll;
    }    

    //그러고도 남은 것들끼리 계산해준다.
    int f = 0;
    int fsize = food_times.size();
    for(int i=0;i<fsize;i++) food_times[i]-=foodTimeAll;
    
    for(int i=0;i<k;i++){
        while(food_times[f]<=0) {
            f++;
            if(f==fsize) f=0;
        }
        food_times[f]--;
        f++;
        if(f==fsize) f=0;
    }
    while(food_times[f]<=0) {
        f++;
        if(f==fsize) f=0;
    }
    int answer = f+1;
    return answer;
}