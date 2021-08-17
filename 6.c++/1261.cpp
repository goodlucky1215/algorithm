#include <iostream>
#include <queue>
#define MAX 100
using namespace std;
int n,m;
int miro[MAX][MAX];
int miroMin[MAX][MAX];
queue<pair<int,int>> findMiro;

void breakWall(int x,int y){
  int moveX[4] = {1,0,-1,0};
  int moveY[4] = {0,1,0,-1};
  for(int i=0;i<4;i++){
    int x1 = x+moveX[i];
    int y1 = y+moveY[i];
    if(x1>=0 && y1>=0 && x1<m && y1<n){
      if(miroMin[x1][y1]>miroMin[x][y]+miro[x1][y1]){
        miroMin[x1][y1]=miroMin[x][y]+miro[x1][y1];
        findMiro.push(make_pair(x1,y1));
      }
    }
  }
}

void start(){
  miro[0][0]=0;
  miroMin[0][0]=0;
  findMiro.push(make_pair(0,0));

  while(!findMiro.empty()){
    int x = findMiro.front().first;
    int y = findMiro.front().second;
    findMiro.pop();
    breakWall(x,y);
  }
}

void input(){
  cin>>n>>m;
  string state;
  for(int i=0;i<m;i++){
    cin>>state;
    for(int j=0;j<n;j++){
      miro[i][j]=state[j]-'0';
      miroMin[i][j]=100000;
    }
  }
  start();
}

int main() {
  input();
  cout<<miroMin[m-1][n-1];
}