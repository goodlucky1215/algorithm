#include <iostream>
#include <deque>
using namespace std;

//깨달은 점
//1. 문제를 잘 읽자..(시간은 따로따로가 아니라 이어지는? 시간이다.)
//2. 마지막 이동은 뱀이 부딪히지만 않으면 부딪힐때까지 뱀은 이동한다.
int inputValue(){
  int n, k;
  cin>>n>>k;
  int stage[101][101]={0,};
  //뱀은 90도씩 꺽고, 시계방향으로 계산
  int direction = 0;
  int x[4] = {0,1,0,-1};
  int y[4] = {1,0,-1,0};
  //사과의 위치
  int a,b;
  for(int i=0;i<k;i++){
    cin>>a>>b;
    stage[a][b] = -1;
  }
  int l;
  cin>>l;
  int theEndGame = 0; //게임이 몇 초에 끝나는지 출력값
  stage[1][1] = 1; //뱀의 위치
  deque<pair<int,int>> deSnake;
  deSnake.push_front(make_pair(1,1));
  //뱀의 방향 변환
  int c=0, c1=0;
  char w;
  for(int i=0;i<=l;i++){
    if(i!=l) cin>>c1>>w;
    else c1 = 20000;
    c=c1-c;
    //c초동안 뱀이 움직임.
    for(int i=0;i<c;i++){
      theEndGame++;
      int x1 = deSnake.front().first+ x[direction];
      int y1 = deSnake.front().second + y[direction];
      if(x1>=1 and x1<=n and y1>=1 and y1<=n){
        if(stage[x1][y1]==1) return theEndGame;
        else if(stage[x1][y1]!=-1){
          //사과가 없다면 뱀은 꼬리는 움직이므로 다시 stage로 만들어줘야함.
          stage[deSnake.back().first][deSnake.back().second] = 0;
          deSnake.pop_back();
        }
        stage[x1][y1] = 1;
        deSnake.push_front(make_pair(x1,y1));
      }else return theEndGame;
    }
    //방향 변경
    if(w=='D') direction = ++direction < 4 ? direction : 0;
    else direction = --direction >=0 ? direction : 3;  
    c=c1;
  }
 return theEndGame;    
}
int main() {
  cout<<inputValue();
}