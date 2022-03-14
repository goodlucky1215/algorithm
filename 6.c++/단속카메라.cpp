#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// 시간복잡도(n)
int solution(vector<vector<int>> routes) {
    int answer = 1;
    sort(routes.begin(),routes.end(),greater<>());
    int camera = routes[0][0];
    for(int i=1;i<routes.size();i++){
        if(routes[i][1]<camera){
            camera = routes[i][0];
            answer++;
        }
    }
    return answer;
}