#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int n, vector<int> weak, vector<int> dist) {
    int answer = 1e9;
    int weakLen = weak.size();
    int distLen = dist.size();
    for(int i=0;i<weakLen;i++){
        weak.push_back(n+weak[i]);
    }
    sort(dist.begin(),dist.end());
    do{
        for(int i=0;i<weakLen;i++){
            int start = weak[i];
            int end = weak[i+weakLen-1];
            for(int j=0;j<distLen;j++){
                start += dist[j];
                if(start>=end) {
                    answer = min(answer,j+1);
                    break;
                }
                int startRe = upper_bound(weak.begin(),weak.end(),start)-weak.begin();
                start = weak[startRe];
            }
        }
    }while(next_permutation(dist.begin(),dist.end()));
    if(answer == 1e9) return -1;
    return answer;
}
int main() {
    
	return 0;
}