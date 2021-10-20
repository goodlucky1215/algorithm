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
      int top = buliding.top();
      buliding.pop();
      while(!buliding.empty()&&buliding.top()==top){
        buliding.pop();
      }
      result++;
    }
    while(b==0&&!buliding.empty()){
      int top = buliding.top();
      buliding.pop();
      while(!buliding.empty()&&buliding.top()==top){
        buliding.pop();
      }
      result++;
    }
    if(b!=0){
      buliding.push(b);
    }
  }
  while(!buliding.empty()){
    int top = buliding.top();
    buliding.pop();
    while(!buliding.empty()&&buliding.top()==top){
      buliding.pop();
    }
    result++;
  }
  cout<<result;
}

int main() {
  start();
}