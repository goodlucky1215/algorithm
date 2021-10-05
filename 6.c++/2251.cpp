#include <iostream>
using namespace std;

bool bowlCheck[203][203];
bool resultCheck[203];

void warter(int bowl[3][2],int putbowl,int getbowl){
  if(bowlCheck[bowl[0][1]][bowl[1][1]]==true) return;
  bowlCheck[bowl[0][1]][bowl[1][1]] = true;
  if(bowl[0][1]==0)resultCheck[bowl[2][1]]=true;
  for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
        if(i!=j){
          int num1 = bowl[0][1];
          int num2 = bowl[1][1];
          int num3 = bowl[2][1];
          if(bowl[i][1]<=(bowl[j][0]-bowl[j][1])) {
            bowl[j][1]+=bowl[i][1];
            bowl[i][1] = 0;
          }else{
            bowl[i][1]-=(bowl[j][0]-bowl[j][1]);
            bowl[j][1]=bowl[j][0];
          }
          warter(bowl,i,j);
          bowl[0][1] = num1;
          bowl[1][1] = num2;
          bowl[2][1] = num3;
        }
    }
  }
}

void start(){
  
  //계산 값 넣기
  int bowl[3][2]={0,};
  for(int i=0;i<3;i++){
    cin>>bowl[i][0];
  }
  bowl[2][1]=bowl[2][0];

  //값 돌리기
  warter(bowl,0,1);

  //결과
  for(int i=0;i<=bowl[2][0];i++){
    if(resultCheck[i]==true) cout<<i<<" ";
  }
}

int main() {
  start();
}