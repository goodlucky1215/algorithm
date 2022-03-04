#include <string>
#include<queue>
#include <vector>

#define up 0
#define dow 1
#define le 2
#define ri 3
using namespace std;

bool check[100][100][4];
int answer = 10000000;
int n;

//현재 위치
struct load{
  int x1, y1, x2, y2;
  int re; //시간
  int shape; //가로는 1 , 세로는 2
};

//가로일때, 왼오위아 이동 시
int x[4][2] = {{1,1},{-1,-1},{0,0},{0,0}};
int y[4][2] = {{0,0},{0,0},{1,1},{-1,-1}};
bool checkMove(int x3,int y3,int x4, int y4,vector<vector<int>> board){
        if(x3>=0 and x3<=n and x4>=0 and x4<=n and y3>=0 and y3<=n and y4>=0 and y4<=n){
            if(board[x3][y3] ==0 and board[x4][y4] ==0 and check[x3][y3][le]==0 and check[x4][y4][ri]==0) {
                check[x3][y3][le]=1;
                check[x4][y4][ri]=1;
                return true;
            }
        }
        return false;
}

bool checkMove1(int x3,int y3,int x4, int y4,vector<vector<int>> board){
        if(x3>=0 and x3<=n and x4>=0 and x4<=n and y3>=0 and y3<=n and y4>=0 and y4<=n){
            if(board[x3][y3] ==0 and board[x4][y4] ==0 and check[x3][y3][up]==0 and check[x4][y4][dow]==0) {
                check[x3][y3][up]=1;
                check[x4][y4][dow]=1;
                return true;
            }
        }
        return false;
}

//가로 => 세로 회전
int xy[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
int xy2[4][2] = {{1,0},{1,0},{0,-1},{0,-1}};
int upDown[4][2] = {{up,dow},{dow,up},{dow,up},{up,dow}};     
bool checkTurn(int x, int y, int x1, int y1, int x2, int y2,vector<vector<int>> board, int k){
  if(x>=0 and x<=n and y>=0 and y<=n and x1>=0 and x1<=n and y1>=0 and y1<=n){
      if(board[x][y]==0 and board[x1][y1]==0 and board[x2][y2]==0 and check[x][y][upDown[k][0]]==0 and check[x1][y1][upDown[k][1]]==0) {
          check[x][y][upDown[k][0]]=1;
          check[x1][y1][upDown[k][1]]=1;
          return true;
      }
    }
  return false;
}

//세로 => 가로 회전
int xy3[4][2] = {{1,0},{1,0},{0,-1},{0,-1}};
int xy4[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
int leRi[4][2] = {{le,ri},{ri,le},{ri,le},{le,ri}};     
bool checkTurn1(int x, int y, int x1, int y1, int x2, int y2,vector<vector<int>> board, int k){
  if(x>=0 and x<=n and y>=0 and y<=n and x1>=0 and x1<=n and y1>=0 and y1<=n){
      if(board[x][y]==0 and board[x1][y1]==0 and board[x2][y2]==0 and check[x][y][leRi[k][0]]==0 and check[x1][y1][leRi[k][1]]==0) {
          check[x][y][leRi[k][0]]=1;
          check[x1][y1][leRi[k][1]]=1;
          return true;
      }
    }
  return false;
}

load loadPut(int x, int y,int x2,int y2,int re,int sh){
    load lo{x, y,x2,y2,re,sh};
    return lo;
}


int solution(vector<vector<int>> board) {

    n = board.size()-1;

    queue<load> qu;

    check[0][0][le] = 1;
    check[0][1][ri] = 1;
    load lo{0,0,0,1,0,1};
    qu.push(lo);

    while(!qu.empty()){
        load lo = qu.front();
        qu.pop();

        if(answer<=lo.re) continue;
        if((lo.x1==n and lo.y1==n) or (lo.x2==n and lo.y2==n)) {
            answer = min(answer,lo.re);
            continue;
        }

        lo.re++;
        if(lo.shape==1) { //가로
            //이동시
            for(int i=0;i<4;i++){
                int x3 = lo.x1+x[i][0];
                int y3 = lo.y1+y[i][0];
                int x4 = lo.x2+x[i][1];
                int y4 = lo.y2+y[i][1];
                if(checkMove(x3,y3,x4,y4,board)){
                    qu.push(loadPut(x3,y3,x4,y4,lo.re,1));
                }
            }
   
            //회전시
            for(int i=0;i<2;i++){
                int x3 = lo.x1+xy[i][0];
                int y3 = lo.y1+xy2[i][0];
                int x4 = lo.x2+xy[i][1];
                int y4 = lo.y2+xy2[i][1];
                if(checkTurn(x3,y3,x4,y4,x3,lo.y1,board,i)) {
                    if(upDown[i][0]==up) qu.push(loadPut(x3,y3,x4,y4,lo.re,2));
                    else qu.push(loadPut(x4,y4,x3,y3,lo.re,2));
                }
            }
            for(int i=2;i<4;i++){
                int x3 = lo.x1+xy[i][0];
                int y3 = lo.y1+xy2[i][0];
                int x4 = lo.x2+xy[i][1];
                int y4 = lo.y2+xy2[i][1];
                if(checkTurn(x3,y3,x4,y4,x4,lo.y2,board,i)) {
                    if(upDown[i][0]==up) qu.push(loadPut(x3,y3,x4,y4,lo.re,2));
                    else qu.push(loadPut(x4,y4,x3,y3,lo.re,2));
                }
            }


    } else {
            
        //이동시
        for(int i=0;i<4;i++){
            int x3 = lo.x1+y[i][0];
            int y3 = lo.y1+x[i][0];
            int x4 = lo.x2+y[i][1];
            int y4 = lo.y2+x[i][1];
            if(checkMove1(x3,y3,x4,y4,board)){
                qu.push(loadPut(x3,y3,x4,y4,lo.re,2));
            }
        }
            
        //회전시
        for(int i=0;i<2;i++){
            int x3 = lo.x1+xy3[i][0];
            int y3 = lo.y1+xy4[i][0];
            int x4 = lo.x2+xy3[i][1];
            int y4 = lo.y2+xy4[i][1];
            if(checkTurn1(x3,y3,x4,y4,lo.x1,y3,board,i)) {
                if(leRi[i][0]==le) qu.push(loadPut(x3,y3,x4,y4,lo.re,1));
                else qu.push(loadPut(x4,y4,x3,y3,lo.re,1));
            }
        }
        for(int i=2;i<4;i++){
            int x3 = lo.x1+xy3[i][0];
            int y3 = lo.y1+xy4[i][0];
            int x4 = lo.x2+xy3[i][1];
            int y4 = lo.y2+xy4[i][1];
            if(checkTurn1(x3,y3,x4,y4,lo.x2,y4,board,i)) {
                if(leRi[i][0]==le) qu.push(loadPut(x3,y3,x4,y4,lo.re,1));
                else qu.push(loadPut(x4,y4,x3,y3,lo.re,1));
            }
        }
   }


}

    return answer;
}