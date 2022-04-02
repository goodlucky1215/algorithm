#include <string>
#include <vector>

using namespace std;

long long solution(int n) {
    int a=1,b=2,i;
    long long answer = 0;
    if (n<=2) answer=n;
    else{
        for (i=3;i<=n;i++){
        answer=(a+b)%1234567;
        a=b;
        b=answer;
    }
    }
    return answer;
}