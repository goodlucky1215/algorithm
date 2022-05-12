#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<long long>> box(5);

vector<vector<long long>> bunHar(long long b){
  if(b==1) return box;
  vector<vector<long long>> boxChange = bunHar(b/2);
  vector<vector<long long>> re1(5);
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      long long t = 0;
      for(int k=0;k<n;k++){
        t+=boxChange[i][k]*boxChange[k][j];
      }
      re1[i].push_back(t%1000);
    }
  }
  if(b%2==1){
    vector<vector<long long>> re2(5);
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        long long t = 0;
        for(int k=0;k<n;k++){
          t+=re1[i][k]*box[k][j];
        }
        re2[i].push_back(t%1000);
      }
    }
    return re2;
  }
  return re1;
}

void startJegob(){
  long long b;
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
  vector<vector<long long>> result = bunHar(b);
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      cout<<result[i][j]%1000<<" ";
    }
    cout<<"\n";
  }
}

int main() {
  startJegob();
}