#include <iostream>
#include <stack>
using namespace std;
string word;
int check[51];

int result(int start,int end){
  int cnt=0;
  for(int i=start;i<end;i++){
    if(word[i]=='('){
      int k = word[i-1]-'0';
      cnt+=k*result(i+1,check[i])-1;
      i=check[i];
      continue;
    }
    cnt++;
  }
  return cnt;
}
void start(){
  cin>>word;
  stack<char> wordput;
  for(int i=0;i<word.length();i++){
    if(word[i]=='('){
      wordput.push(i);
    }else if(word[i]==')'){
      check[wordput.top()]=i;
      wordput.pop();
    }
  }
  cout<<result(0,word.length());
}

int main() {
  start();
}