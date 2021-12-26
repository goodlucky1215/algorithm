#include <iostream>
using namespace std;

int r,c,t;
int ground[51][51];
int robot[2];

int resultSmoke(){
  int cnt = 0;
  for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
     cnt+=ground[i][j];
    }
  }
  return cnt;
}

void smokeCopy(int groundR[51][51]){
  for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
      ground[i][j] = groundR[i][j];
    }
  }
}

void smokeCleanUp(int groundR[51][51],int x){
  int fir = 0;
  int sec = 0;
  for(int i=1;i<c;i++){
    fir = sec;
    sec = groundR[x][i];
    groundR[x][i] = fir;
  }
  for(int i=x-1;i>=0;i--){
    fir = sec;
    sec = groundR[i][c-1];
    groundR[i][c-1] = fir;
  }
  for(int i=c-2;i>=0;i--){
    fir = sec;
    sec = groundR[0][i];
    groundR[0][i] = fir;
  }
  for(int i=1;i<x;i++){
    fir = sec;
    sec = groundR[i][0];
    groundR[i][0] = fir;
  }
}

void smokeCleanDown(int groundR[51][51],int x){
  int fir = 0;
  int sec = 0;
  for(int i=1;i<c;i++){
    fir = sec;
    sec = groundR[x][i];
    groundR[x][i] = fir;
  }
  for(int i=x+1;i<r;i++){
    fir = sec;
    sec = groundR[i][c-1];
    groundR[i][c-1] = fir;
  }
  for(int i=c-2;i>=0;i--){
    fir = sec;
    sec = groundR[r-1][i];
    groundR[r-1][i] = fir;
  }
  for(int i=r-2;i>x;i--){
    fir = sec;
    sec = groundR[i][0];
    groundR[i][0] = fir;
  }
}

void smokeMove(){
  int groundCheck[51][51]={0,};
  int x[4] = {0,0,1,-1};
  int y[4] = {1,-1,0,0};
  for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
      if(ground[i][j]>0){
        int smoke = ground[i][j]/5;
        int su=0;
        for(int k=0;k<4;k++){
          int x1 = i+x[k];
          int y1 = j+y[k];
          if(x1>=0 and x1<r and y1>=0 and y1<c and ground[x1][y1]!=-1 
          and !(y1==0 and (robot[0]==x1 or robot[1]==x1))){
            su++;
            groundCheck[x1][y1]+=smoke;
          }
        }
        groundCheck[i][j]+=ground[i][j]-(smoke)*su;
      }
    }
  }
  //공기청정기 가동
  smokeCleanUp(groundCheck,robot[0]);
  smokeCleanDown(groundCheck,robot[1]);
  //값 복사
  smokeCopy(groundCheck);
}

void putMap(){
  cin>>r>>c>>t;
  for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
      cin>>ground[i][j];
    }
  }
  for(int i=0;i<r;i++){
    if(ground[i][0]==-1){
      robot[0]=i;
      robot[1]=i+1;
      break;
    }
  }
  for(int i=0;i<t;i++){
    //확산
    smokeMove();
  }
  cout<<resultSmoke();
}

int main() {
  putMap();
} 