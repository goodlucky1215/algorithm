#include <iostream>
#include <vector>
using namespace std;

//배운점
//1. 규칙적인 부분이 나오면 규칙을 찾자
//어떻게든 찾아야한다!!

vector<int> dragon;
int dragonSu[11];

//0~10세대까지 구성
void makeSede(){
  dragon.push_back(0);
  dragonSu[0] = 1;
  for(int i=1;i<=10;i++){
    int dragonSize = dragon.size();
    dragonSu[i]=dragonSize*2;
    for(int j=dragonSize-1;j>=0;j--){
      int a = (dragon[j] + 1)%4;
      dragon.push_back(a);
    }
  }
}

void inputValue(){
  int n,x,y,d,g;
  cin>>n;
  makeSede();
  int x1[4] = {1,0,-1,0};
  int y1[4] = {0,-1,0,1};

  int box[101][101] = {0,};
  //모든 좌표를 저장
  for(int i=0;i<n;i++){
    cin>>x>>y>>d>>g;
    box[x][y]=1;
    for(int i=0;i<dragonSu[g];i++){
      int curve = (dragon[i] + d)%4;
      x += x1[curve];
      y += y1[curve];
      box[x][y]=1;
    }
  }


  //출력값
  int result = 0;
  int x2[3] = {1,0,1};
  int y2[3] = {0,1,1};
  for(int i=0;i<100;i++){
    for(int j=0;j<100;j++){
      if(box[i][j]==1){
        int r = 0;
        for(int k=0;k<3;k++){
          int x3 = i + x2[k];
          int y3 = j + y2[k];
          if(box[x3][y3]!=1){
            r = 1;
            break;
          }
        }
        if(r==0) result++;
      }
    }
  }

  cout<<result<<"\n";
}
int main() {
  inputValue();
}