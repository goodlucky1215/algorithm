#include <iostream>
using namespace std;

bool result;
int marketSu;


bool calBear(int startX,int startY,int endX,int endY){
  int walk = abs(endX-startX)+abs(endY-startY);
  if(walk<=1000) return true;
  return false;
}

void festivalGo(int startX,int startY,int marketPlace[][3],int endX,int endY){
  if(result) return;
  if(calBear(startX, startY,endX, endY)==true){
    result=true;
    return;
  }
  for(int i=0;i<marketSu;i++){
    if(marketPlace[i][2]==0 and calBear(marketPlace[i][0], marketPlace[i][1],startX, startY)==true){
      marketPlace[i][2]=1;
      festivalGo(marketPlace[i][0], marketPlace[i][1], marketPlace, endX, endY);
    }
  }

}
void startTest(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin>>marketSu;
  int marketPlace[marketSu][3];
  int startX,startY,endX,endY;
  cin>>startX>>startY;
  for(int i=0;i<marketSu;i++){
    cin>>marketPlace[i][0]>>marketPlace[i][1];
    marketPlace[i][2]=0;
  }
  cin>>endX>>endY;
  result=false;
  festivalGo(startX,startY,marketPlace,endX,endY);
  if(result==true)cout<<"happy"<<"\n";
  else cout<<"sad"<<"\n";
}
void putTest(){
  int testcase;
  cin>>testcase;
  for(int i=0;i<testcase;i++){
    startTest();
  }
}

int main() {
  putTest();
}