#include <iostream>
using namespace std;
int box[400010];
int su[100010];

int minValue(int start,int end,int node,int left,int right){
  if(left>end || right<start) return 1000000001;
  if(left<=start && right>=end) return box[node];
  int mid = (start+end)/2;
  return min(minValue(start,mid,node*2,left,right),minValue(mid+1,end,node*2+1,left,right));
}

int segment(int start,int end,int n){
  if(start==end) return box[n]=su[start];
  int mid = (start+end)/2;
  return box[n] = min(segment(start,mid,n*2),segment(mid+1,end,n*2+1)); 
}

void input(){
  cin.tie(NULL); ios_base::sync_with_stdio(0);
  int n;
  int m;
  cin>>n>>m;
  for(int i=1;i<=n;i++){
    cin>>su[i];
  }
  segment(1,n,1);
  int a,b;
  for(int i=0;i<m;i++){
    cin>>a>>b;
    cout<<minValue(1,n,1,a,b)<<"\n";
  }
}

int main() {
  input();
}