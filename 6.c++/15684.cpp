#include <iostream>
using namespace std;

int n,h,m;
int sadari[32][12];
bool result = false;

bool sadariCheck(){
  for(int i=1;i<=n;i++){
    int x = 1;
    int y = i;
    while(x<=m){
      if(sadari[x][y]==1){
        y++;
      }else if(sadari[x][y-1]==1){
        y--;
      }
      x++;
    }
    if(i!=y) return false;
  }
  return true;
}

void sadariAdd(int su, int maxSu,int start,int end){
  if(result) return;
  if(su==maxSu){
    //사다리 갯수만큼 추가했다면 확인하기
    result = sadariCheck();
    return;
  }
  for(int i=start;i<=start;i++){
    for(int j=end;j<n;j++){
      if(sadari[i][j-1]!=1 and sadari[i][j+1]!=1  and sadari[i][j]!=1) {
        sadari[i][j]=1;
        sadariAdd(su+1,maxSu,i,j+1);
        sadari[i][j]=0;
      }
    }
  }
  for(int i=start+1;i<=m;i++){
    for(int j=1;j<n;j++){
      if(sadari[i][j-1]!=1 and sadari[i][j+1]!=1 and sadari[i][j]!=1) {
        sadari[i][j]=1;
        sadariAdd(su+1,maxSu,i,j+1);
        sadari[i][j]=0;
      }
    }
  }
}

int inputValue(){
  cin>>n>>h>>m;
  int a,b;
  //사다리 두기
  for(int i=0;i<h;i++){
    cin>>a>>b;
    sadari[a][b] = 1;
  }
  //사다리 추가 개수를 i로 하기
  for(int i=0;i<=3;i++){
    sadariAdd(0,i,1,1);
    if(result) return i;
  }
  return -1;
}

int main() {
  cout<<inputValue()<<"\n";
}