#include <iostream>
#include <vector>
#include <set>
using namespace std;

struct lineSu{
  int line;
  int su;
};

int n;
vector<vector<lineSu>> treeLine(100001);
bool check[100001];
int result = 0;
int maxLine = 1;
void dfs(int i,int total){
    if(result<total){
        result = total;
        maxLine = i;
    }
  for(lineSu j:treeLine[i]){
    if(check[j.line]==false){
      check[j.line]=true;
      int t = j.su+total;
      dfs(j.line,t);
      check[j.line]=false;
    }
  }
}
void start(){
  cin>>n;

  for(int i=0;i<n;i++){
    int a;
    cin>>a;
    while(true){
      int b;
      cin>>b;
      if(b==-1) break;
      lineSu linesu;
      linesu.line = b;
      cin>>linesu.su;
      
      treeLine[a].push_back(linesu);
    }
  }

  check[1] = true;
  dfs(1,0);
  check[1] = false;

  check[maxLine] = true;
  dfs(maxLine,0);
    
  cout<<result;
}
int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  start();
}