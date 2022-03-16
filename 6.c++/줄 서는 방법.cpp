#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, long long k) {
    vector<int> answer;
    long long person[n+1];
    person[1] = 1;
    //자리에 따른 될 수 있는 경우의 수
    for(int i=2;i<n;i++){
        person[i] = person[i-1]*i;
    }
    //최소값
    int minV = 1;
    //넣은 값인지 체크
    bool check[21] = {0,};
    for(int i=n-1;i>0;i--){
        if(k<=person[i]){
            answer.push_back(minV);
            check[minV] = 1;
            for(int j=minV+1;j<=n;j++){
                if(check[j]==0){
                    minV = j;
                    break;
                }
            }
            continue;
        }
        int personPlace = k/person[i]; //minV보다 몇번째 큰 수인지
        if(k%person[i] == 0) personPlace-=1; //그 숫자의 마지막 값을 의미하게 됨! 
        k-=(long long)personPlace*person[i];
        int minVNext = minV;
        for(int j1=0;j1<personPlace;j1++){
            for(int j=minVNext+1;j<=n;j++){
                if(check[j]==0){
                    minVNext = j;
                    break;
                }
            }
        }
        answer.push_back(minVNext);
        check[minVNext] = 1;
    }
    answer.push_back(minV);
    return answer;
}