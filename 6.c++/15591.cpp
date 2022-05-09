#include <iostream>
#include <queue>
#include <map>
using namespace std;

vector<map<int,int>> mootube(5001);

int getMooTubeSu(int k,int v){
  int result = 0;
  bool check[5001] = {0,};
  check[v] = 1;
  queue<int> quMooTube;
  quMooTube.push(v);

  while(!quMooTube.empty()){
    int v1 = quMooTube.front();
    quMooTube.pop();
    
    for(auto iter = mootube[v1].begin(); iter!=mootube[v1].end();iter++){
      if(check[iter->first]==0 and iter->second >=k) {
        quMooTube.push(iter->first);
        check[iter->first]=1;
        result++;
      }
    }    
  }
  
  return result;
}

void mootubeStart(){
  int n,q;
  cin>>n>>q;
  n++;

  for(int i=0;i<n-2;i++){
    int t1, t2, usado;
    cin>>t1>>t2>>usado;
    mootube[t1][t2] = usado;  
    mootube[t2][t1] = usado;  
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