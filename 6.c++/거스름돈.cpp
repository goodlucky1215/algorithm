#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> money) {
    int answer = 0;
    int pay[100001];
    pay[0]=1;
    for(int i:money){
        for(int j=i;j<=n;j++){
            pay[j] = (pay[j]+pay[j-i])%1000000007;
        }
    }
    answer = pay[n];
    return answer;
}