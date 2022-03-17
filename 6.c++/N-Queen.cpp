#include <string>
#include <vector>

using namespace std;

int q[13];
int answer;
int queenSu;
bool checkQueen(int queen, int place){
    for(int i=1,j=queen-1;i<queen;i++,j--){
        if(q[i]==place || q[i]+j==place || q[i]-j==place) return false;
    }
    return true;
}

void goQueen(int queen){
    if(queenSu==queen) {
        answer++;
        return;
    }
    for(int i=1;i<queenSu;i++){
        if(checkQueen(queen,i)){ 
            q[queen]=i;
            goQueen(queen+1);
        }
    }
}
int solution(int n) {
    queenSu=n+1;
    for(int i=1;i<=n;i++){
        q[1]=i;
        goQueen(2);
    }
    return answer;
}