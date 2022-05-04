#include <iostream>
#include <queue>
using namespace std;

int mootube[5001][5001];
int n;

int getMooTubeSu(int k,int v){
  int result = 0;
  for(int i =1;i<n;i++){
    if(mootube[v][i]>=k) result++;
  }
  return result;
}

void minNetwork(int start,int end){
  bool su[n];
  queue<int> qu;
  queue<int> quMin;
  for(int i=1;i<n;i++){
    su[i] = false;
    if(mootube[start][i]!=0){
      qu.push(i);
      quMin.push(mootube[start][i]);
    }
  }
  mootube[start][end] = 1000000001;
  su[start] = true;
  while(!qu.empty()){
    int s = qu.front();
    int sMin = quMin.front();
    qu.pop();
    quMin.pop();
    su[s] = true;
    for(int i=1;i<n;i++){
      if(i==end and mootube[s][i]!=0){
        mootube[start][end] = min(mootube[s][i],mootube[start][end]);
        mootube[start][end] = min(sMin,mootube[start][end]);
        continue;
      }
      if(su[i]==false and mootube[s][i]!=0){
        qu.push(i);
        quMin.push(min(mootube[s][i],sMin));
      }
    }
  }
  mootube[end][start] = mootube[start][end];
}

void mootubeStart(){
  cin>>n;
  n++;
  int q;
  cin>>q;

  for(int i=0;i<n-2;i++){
    int t1, t2, usado;
    cin>>t1>>t2>>usado;
    mootube[t1][t2] = usado;
    mootube[t2][t1] = usado;    
  }

  //모든 동영상의 최솟값의 연관성을 찾아준다.
  for(int i=1;i<n;i++){
    for(int j=1;j<n;j++){
      if(i==j) continue;
      if(mootube[i][j]!=0) continue;
      minNetwork(i,j);
    }
  }
  
  //q개의 질문, 동영상 v와 관련된 동영상이 k이상인 동영상의 수
  for(int i=0;i<q;i++){
    int k, v;
    cin>>k>>v;
    int result = getMooTubeSu(k,v);
    cout<<result<<"\n";
  }  
}

int main() {
  mootubeStart();
}