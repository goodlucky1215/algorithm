#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> tree(1003);

//정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
void dfs(bool check[],int v){
  cout<<v<<" ";
  check[v]=1;
  for(int i:tree[v]){
    if(!check[i]){
      dfs(check,i);
    }
  }
}

void dfsStart(int v){
  bool check[1003] = {0,};
  dfs(check,v);
}

void bfs(int n,int v){
  bool check[1003] ={0,};
  queue<int> num;
  vector<int> result;
  num.push(v);
  while(!num.empty()){
    int fro = num.front();
    num.pop();
    if(!check[fro]){
      check[fro]=true;
      result.push_back(fro);
      for(int i:tree[fro]){
        if(!check[i])num.push(i);
      }
    }
  }
  for(int i:result) cout<<i<<" "; 
}

void input(){
  int n,m,v;
  cin>>n>>m>>v;
  int a,b;
  for(int i=0;i<m;i++){
    cin>>a>>b;
    tree[a].push_back(b);
    tree[b].push_back(a);
  }
  for(int i=1;i<=n;i++) sort(tree[i].begin(),tree[i].end());
  dfsStart(v);
  cout<<"\n";
  bfs(n,v);
}
int main() {
  input();
} 