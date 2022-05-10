#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> box(5);

vector<vector<int>> bunHar(int b){
  if(b/2==0) return box;
  vector<vector<int>> boxChange = bunHar(b/2);
  cout<<boxChange.size();
  vector<vector<int>> re1(5);
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      int t = 0;
      for(int k=0;k<n;k++){
        t+=boxChange[i][k]*boxChange[i][k];
        t%=1000;
      }
      re1[i][j] = t;
    }
  }
  if(b%2==1){
    vector<vector<int>> re2(5);
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        int t = 0;
        for(int k=0;k<n;k++){
          t+=re1[i][k]*box[i][k];
          t%=1000;
        }
        re2[i][j] = t;
      }
    }
    return re2;
  }
  return re1;
}

void startJegob(){
  int b;
  //값 입력
  cin>>n>>b;
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      int a;
      cin>>a;
      box[i].push_back(a);
    }
  }
  //분할 정복
  vector<vector<int>> result = bunHar(b);
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
    //  cout<<result[i][j]<<" ";
    }
    cout<<"\n";
  }
}

int main() {
  startJegob();
}