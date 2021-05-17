#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector <pair<int,int>> num;
int n;
bool sort_n(pair<int,int> a,pair<int,int> b){
  if(a.second!=b.second) return a.second<b.second;
  return a.first<b.first;
}
void result(){
  sort(num.begin(),num.end(),sort_n);
  int re = num[1].first-num[0].first+num[n-1].first-num[n-2].first;
  for(int i=1;i<n-1;i++){
    if(num[i].second==num[i-1].second&&num[i].second==num[i+1].second){
      re+=min(num[i].first-num[i-1].first,num[i+1].first-num[i].first);
    }
    else if(num[i].second==num[i-1].second)re+=num[i].first-num[i-1].first;
    else if(num[i].second==num[i+1].second)re+=num[i+1].first-num[i].first;
  }
  cout<<re<<"\n";
}
void push_num(){
  cin>>n;
  for(int i=0;i<n;i++){
    int a,b;
    cin>>a>>b;
    num.push_back(pair(a,b));
  }
  result();
}
int main() {
  push_num();
}