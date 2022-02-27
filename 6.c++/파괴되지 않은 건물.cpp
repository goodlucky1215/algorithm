#include <string>
#include <vector>

using namespace std;

// 시간복잡도 O(K+3*N*M)
// 누적합이라는 것을 알게됨!
int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int boardSkill[1001][1001]={0,};
    for(int i=0;i<skill.size();i++){ //K
        if(skill[i][0]==1) skill[i][5]= -skill[i][5];
        boardSkill[skill[i][1]][skill[i][2]] += skill[i][5];
        boardSkill[skill[i][1]][skill[i][4]+1] -= skill[i][5];
        boardSkill[skill[i][3]+1][skill[i][2]] -= skill[i][5];
        boardSkill[skill[i][3]+1][skill[i][4]+1] += skill[i][5];
    }
    for(int i=0;i<board[0].size();i++){
        for(int j=1;j<board.size();j++){
            boardSkill[j][i] += boardSkill[j-1][i];
        }
    }
    for(int i=0;i<board.size();i++){
        for(int j=1;j<board[0].size();j++){
            boardSkill[i][j] += boardSkill[i][j-1];
        }
    }
    int answer = 0;
    for(int i=0;i<board.size();i++){ //N
        for(int j=0;j<board[0].size();j++){ //M
            board[i][j] += boardSkill[i][j];
            if(board[i][j]>0) answer++;
        }
    }
    return answer;
}