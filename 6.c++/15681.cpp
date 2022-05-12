#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> vec(100001);
int result[100001];
bool check[100001];

int subRootFind(int r){
  result[r] = 1;
  for(int i:vec[r]){
    if(!check[i]){
      check[i] = true;
      result[r] += subRootFind(i); 
    }
  }
  return result[r];
}

void start(){
  int n,r,q;
  cin>>n>>r>>q;
  for(int i=0;i<n-1;i++){
    int a,b;
    cin>>a>>b;
    vec[a].push_back(b);
    vec[b].push_back(a);
  }

  check[r]=true;
  subRootFind(r);

  for(int i=0;i<q;i++){
    int a;
    cin>>a;
    cout<<result[a]<<"\n";
  }
}
int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  start();
}