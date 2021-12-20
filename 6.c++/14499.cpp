#include <iostream>
#include <string>
using namespace std;

char map[100][100];
int n,m,x,y;
char dice[7];
string garo="4136",sero="2156";

//주사위 바닥면 인덱스
int findDiceBottom(){
  if(garo[1]=='1') return 6;
  else if(garo[1]=='2') return 5;
  else if(garo[1]=='3') return 4;
  else if(garo[1]=='4') return 3;
  else if(garo[1]=='5') return 2;
  else return 1;
}

//주사위 이동
void roll(int diceNum){
  //동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
  switch(diceNum){
    case 1:{
      if(m>y+1){
        y++;
        string garo1 = garo;
        garo[0] =garo1[3];
        garo[1] =garo1[0];
        garo[2] =garo1[1];
        garo[3] =garo1[2];
        sero[1] = garo[1];
        sero[3] = garo[3];
      }else return;
      break;
    }
    case 2:{
      if(0<=y-1){
        y--;
        string garo1 = garo;
        garo[0] =garo1[1];
        garo[1] =garo1[2];
        garo[2] =garo1[3];
        garo[3] =garo1[0];
        sero[1] =garo[1];
        sero[3] = garo[3];
      }else return;
      break;
    }
    case 3:{
      if(0<=x-1){
        x--;
        string sero1 = sero;
        sero[0] =sero1[1];
        sero[1] =sero1[2];
        sero[2] =sero1[3];
        sero[3] =sero1[0];
        garo[1] = sero[1];
        garo[3] = sero[3];
      }else return;
      break;
    }
    case 4:{
      if(n>x+1){
        x++;
        string sero1 = sero;
        sero[0] =sero1[3];
        sero[1] =sero1[0];
        sero[2] =sero1[1];
        sero[3] =sero1[2];
        garo[1] = sero[1];
        garo[3] = sero[3];
      }else return;
      break;
    }
  }
  //주사위 바닥면 인덱스
  int diceBottom = findDiceBottom();
  if(map[x][y]=='0'){
    map[x][y] = dice[diceBottom];
  }else{
    dice[diceBottom] = map[x][y];
    map[x][y] = '0';
  }
  cout<<dice[garo[1]-'0']<<"\n";
}

void start(){
  int k;
  cin>>n>>m>>x>>y>>k;
  //주사위 초기화
  for(int i=1;i<=6;i++) dice[i]='0';
  //지도에 적힌 숫자
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      cin>>map[i][j];
    }
  }
  //주사위 동서남북이동
  int diceNum;
  for(int i=0;i<k;i++){
    cin>>diceNum;
    roll(diceNum);
  }
}

int main() {
  start();
} 