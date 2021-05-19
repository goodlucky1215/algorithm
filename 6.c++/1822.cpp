#include <iostream>
#include <set>
using namespace std;
int main() {
  ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  int a,b,n;
  cin>>a>>b;
  set <int> num;
  int s;
  for(int i=0;i<a;i++){
    cin>>s;
    num.insert(s);
  }
  for(int i=0;i<b;i++){
    cin>>s;
    if(num.find(s)!=num.end()) num.erase(s);
  }
  cout<<num.size()<<"\n";
  for(auto i:num) cout<<i<<" ";
}