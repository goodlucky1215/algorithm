#include <string>
#include <vector>
#include <deque>
using namespace std;

int solution(vector<int> stones, int k) {
    deque<int> de;
    de.push_back(0);
    for(int i=0;i<k;i++){
        while(!de.empty() and stones[de.back()]<=stones[i]){
            de.pop_back();
        }
        de.push_back(i);
    }
    int answer = stones[de.front()];
    for(int i=k;i<stones.size();i++){
        while(!de.empty() and stones[de.back()]<=stones[i]) de.pop_back();
        while(!de.empty() and i-de.front()>=k) de.pop_front();
        de.push_back(i);
        answer = min(answer, stones[de.front()]);
    }    
    return answer;
}