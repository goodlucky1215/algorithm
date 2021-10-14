#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int x1[4]={0,0,-1,1};
int y1[4]={1,-1,0,0};
int result;
bool stuCheck[26];
char stuPlace[5][5];

bool sutBool(int n){
  int cnt=0;
  queue<pair<int,int>> qu;
  qu.push(pair(n/5,n%5));
  bool stuCheck1[5][5]={0,};
  while(!qu.empty()){
    int x2 = qu.front().first;
    int y2 = qu.front().second;
    stuCheck1[x2][y2]=true;
    qu.pop();
    cnt++;
    for(int i=0;i<4;i++){
      int x3 = x2+x1[i];
      int y3 = y2+y1[i];
      if(x3>=0 and x3<5 and y3>=0 and y3<5 and stuCheck[x3*5+y3] and stuCheck1[x3][y3]==false){
        qu.push(pair(x3,y3));
        stuCheck1[x3][y3]=true;
      }
    }
  }
  if(cnt==7) return true;
  return false;
}
void princess(int n,int somPa,int su){
  if(su==7){
    if(somPa>=4&&sutBool(n))result++;
    return;
  }
  for(int i=n; i<25; i++){
    if(stuCheck[i]==false){
        stuCheck[i] = true;
        if(stuPlace[i/5][i%5]=='S') princess(i,somPa+1,su+1);
        else  princess(i,somPa,su+1);
        stuCheck[i] = false;
    }
  }
}
void putStart(){
  for(int i=0;i<5;i++){
    for(int j=0;j<5;j++){
      cin>>stuPlace[i][j];
    }
  }

  princess(0,0,0);
  
  cout<<result;
}

int main() {
  putStart();  
}