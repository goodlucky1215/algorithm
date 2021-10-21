#include <iostream>
#include <stack>
using namespace std;

void start(){
  int n;
  cin>>n;
  int result=0;
  stack<int> buliding;
  int a,b;
  for(int i=0;i<n;i++){
    cin>>a>>b;
    while(!buliding.empty()&&buliding.top()>b){
      buliding.pop();
      result++;
    }
    if(!buliding.empty()&&buliding.top()==b) continue;
    buliding.push(b);
  }
  while(!buliding.empty()){
    if(buliding.top()!=0)result++;
    buliding.pop();
  }
  cout<<result;
}

int main() {
  start();
}