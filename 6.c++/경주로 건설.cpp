#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<vector<int>> board) {
    int n = board.size();
    // 0이면 위아래, 1이면 앞뒤방향의미
    int check[26][26][2] = {0,};
    int xy[2] = {1, -1};
    queue<vector<int>> qu;
    //처음에 나아가는 방향 담기
    if(board[0][1]==0) {
        qu.push({0,1,1});
        check[0][1][1]=100;
    }
    if(board[1][0]==0) {
        qu.push({1,0,0});
        check[1][0][0]=100;
    }
    while(!qu.empty()){
        vector<int> vec = qu.front();
        qu.pop();
        int coin = check[vec[0]][vec[1]][vec[2]]+100;
        int coin1 = coin,coin2 = coin;
        //위아래로 가는중이면 앞뒤로 갈 시 500원 추가, 앞뒤로 가는중이면 위아래로 갈 시 500원 추가
        if(vec[2]==0) coin2+=500;
        else coin1 += 500;
        for(int i=0;i<2;i++){
            int x1 = vec[0]+xy[i];
            int y1 = vec[1];
            if(!(x1==0 and y1==0) and x1>=0 and y1>=0 and x1<n and y1<n and board[x1][y1]==0 and (check[x1][y1][0]==0 or (check[x1][y1][0]!=0 and coin<check[x1][y1][0]))){
                check[x1][y1][0] = coin1;
               qu.push({x1,y1,0});
            }
        }
        for(int i=0;i<2;i++){
            int x1 = vec[0];
            int y1 = vec[1]+xy[i];
            if(!(x1==0 and y1==0) and x1>=0 and y1>=0 and x1<n and y1<n and board[x1][y1]==0 and (check[x1][y1][1]==0 or (check[x1][y1][1]!=0 and coin<check[x1][y1][1]))){
                check[x1][y1][1] = coin2;
               qu.push({x1,y1,1});
            }
        }
    }
    int answer = 0;
    if(check[n-1][n-1][1]==0)answer = check[n-1][n-1][0];
    else if(check[n-1][n-1][0]==0)answer = check[n-1][n-1][1];
    else answer = min(check[n-1][n-1][0],check[n-1][n-1][1]);
    return answer;
}