#include <iostream>
#include <algorithm>
using namespace std;
struct point{
  int x;
  int y;
};

point p[1000000];
int n;

void result(){
  long long su=0;
  int left = p[0].x;
  int right = p[0].y;
  for(int i=1;i<n;i++){
    if(right>=p[i].x) right = max(p[i].y,right);
    else{
      su+=right-left;
      left = p[i].x;
      right = p[i].y;
    }
  }
  cout<<su+right-left;
}

bool cmp(point a,point b){
  if(a.x==b.x){
    return a.y<b.y;
  }
  return a.x<b.x;
}

void input(){
  cin.tie(NULL); ios_base::sync_with_stdio(0);
  cin>>n;
  for(int i=0;i<n;i++){
    cin>>p[i].x>>p[i].y;
  }
  sort(p,p+n,cmp);
  result();
}
int main() {
  input();
}