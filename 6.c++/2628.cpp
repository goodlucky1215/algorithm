#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int garo,sero;
int n;
vector <int> g;
vector <int> s;
void result(){
  sort(g.begin(),g.end());
  sort(s.begin(),s.end());
  int g_max=0;
  int s_max=0;
  if(g.size()==0) g_max=garo;
  else{
    g_max = g[0];
    for(int i=0;i<g.size()-1;i++){
      g_max = max(g_max,g[i+1]-g[i]);
    }
    g_max = max(g_max,garo-g[g.size()-1]);
  }
  if(s.size()==0) s_max=sero;
  else{
    s_max = s[0];
    for(int i=0;i<s.size()-1;i++){
      s_max = max(s_max,s[i+1]-s[i]);
    }
    s_max = max(s_max,sero-s[s.size()-1]);
  }
  cout<<s_max*g_max<<"\n";
}
void push_num(){
  cin>>sero>>garo;
  cin>>n;
  for(int i=0;i<n;i++){
    int a,b;
    cin>>a>>b;
    if(a==0)g.push_back(b);
    else s.push_back(b);
  }
  result();
}
int main() {
  push_num();
}