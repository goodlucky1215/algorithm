#include <string>
#include <vector>

using namespace std;

int x4[4]={0,0,-1,1};
int y4[4]={1,-1,0,0};
int x;
int y;

//더 이상 갈 곳이 없다면
bool isFinished(vector<vector<int>> board, int x1, int y1){
    for(int i=0;i<4;i++){
        int ny = y1+y4[i];
        int nx = x1+x4[i];
        if(nx>=0 and nx<x and ny>=0 and ny<y and board[nx][ny]==1) return false;
    }
    return true;
}

pair<bool,int> movePlayer(vector<vector<int>> board,int x1,int y1,int x2,int y2){
    if(isFinished(board,x1,y1)) return {false,0}; //A가 지는 거고 
    if(y1==y2 && x1==x2) return {true,1}; //B가 지는 거고
    
    bool canWin = false;
    int minTurn = 10000, maxTurn = 0;
    
    for(int i=0;i<4;i++){
        int ny = y1+y4[i];
        int nx = x1+x4[i];
        if(nx>=0 and nx<x and ny>=0 and ny<y and board[nx][ny]==1){
            board[x1][y1] = 0;
            pair<bool, int> res = movePlayer(board, x2,y2,nx,ny);
            board[x1][y1] = 1;
            
            if(res.first == false){
                canWin = true;
                minTurn = min(minTurn, res.second); //승리할 시 최소턴 
            }
            else if(canWin == false){
                maxTurn = max(maxTurn, res.second); //패배할 시 최대턴
            }
        }
    }
    
    int turn = canWin ? minTurn : maxTurn;
    return {canWin,1+turn};
}

int solution(vector<vector<int>> board, vector<int> aloc, vector<int> bloc) {
    x = board.size();
    y = board[0].size();

    return movePlayer(board,aloc[0],aloc[1],bloc[0],bloc[1]).second;
}