#include <iostream>
#include <set>
using namespace std;
int cardnum, su;
string card[10];
int use[10];
set<string> re;
void result(string number,int end){
  if(end==su){
    re.insert(number);
  }
  for(int i=0;i<cardnum;i++){
    if(use[i]==0){
      string a = card[i];
      use[i]=1;
      result(number+card[i],end+1);
      use[i]=0;
    }
  }
}

void push_num(){
  cin>>cardnum>>su;
  for(int i=0;i<cardnum;i++){
    cin>>card[i];
  }
  result("",0);
}
int main() {
  push_num();
  cout<<re.size();
