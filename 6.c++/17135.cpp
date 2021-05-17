#include <iostream>
using namespace std;
int row = 0; 
int col = 0;
int attack = 0;
int cnt_max=0;
struct enemy{
  int x=-1;
  int y=-1;
};
enemy enemy_find(int start,int archer,int attack,int castle[16][16]){
  enemy result;
  for(int k=1;k<=attack;k++){
    if(start-k>=0&&archer-attack+k>=0&&castle[start-k][archer-attack+k]==1) {
      result.x=start-k;
      result.y=archer-attack+k;
      return result;
    }
  }
  for(int k=attack-1;k>=1;k--){
    if(start-k>=0&&archer+attack-k<col&&castle[start-k][archer+attack-k]==1){
      result.x=start-k;
      result.y=archer+attack-k;
      return result;
    }
  }
  return result;
}
void castle_defence(int start,int archer1,int archer2,int archer3,int castle1[16][16]){
  int castle[16][16];
  for(int i=0;i<row;i++){
    for(int j=0;j<col;j++){
      castle[i][j]= castle1[i][j];
    }
  }
  int cnt=0;
  for(int i=0;i<row;i++,start--){
    enemy result1,result2,result3;
    for(int j=1;j<=attack;j++){
      result1 = enemy_find(start,archer1,j,castle);
      if(result1.x==-1) continue;
      else break;
    }
    for(int j=1;j<=attack;j++){
      result2 = enemy_find(start,archer2,j,castle);
      if(result2.x==-1) continue;
      else break;
    }
    for(int j=1;j<=attack;j++){
      result3 = enemy_find(start,archer3,j,castle);
      if(result3.x==-1) continue;
      else break;
    }
    if(castle[result1.x][result1.y]==1){
      castle[result1.x][result1.y]=0;
      cnt++; 
    }
    if(castle[result2.x][result2.y]==1){
      castle[result2.x][result2.y]=0;
      cnt++; 
    }
    if(castle[result3.x][result3.y]==1){
      castle[result3.x][result3.y]=0; 
      cnt++;
    }
  }
  cnt_max=max(cnt_max,cnt);
}
void input_num(){
  cin>>row>>col>>attack;
  int castle[16][16];
  for(int i=0;i<row;i++){
    for(int j=0;j<col;j++){
      cin>>castle[i][j];
    }
  }
  int archer1,archer2,archer3;
  for(int i=0;i<col-2;i++){
    archer1=i;
    for(int j=i+1;j<col-1;j++){
      archer2=j;
      for(int k=j+1;k<col;k++){
        archer3=k;
        castle_defence(row,archer1,archer2,archer3,castle);
      }
    }
  }
  cout<<cnt_max;
}
int main() {
  input_num();
}