#include <iostream>
#include <list>
#include<vector>
#include<algorithm>
using namespace std;
int n;
vector<string> num;

bool rule(string a,string b){
  int a_len=a.length();
  int b_len=b.length(); 
  if(a_len!=b_len){
    if(a_len<b_len) return true;
    else if(a_len>b_len) return false;
  }
  int a_num=0;
  int b_num=0;
  for(int i=0;i<a_len;i++){
    if('1'<=a[i] and a[i]<='9')a_num+=a[i]-'0';
  }
  for(int j=0;j<b_len;j++){
    if('1'<=b[j] and b[j]<='9')b_num+=b[j]-'0';
  }
  if(a_num>b_num) return false;
  else if(a_num<b_num) return true;
  return a<b;
}

void start(){
  sort(num.begin(),num.end(),rule);
  list<string>::iterator iter;
  for(int i =0;i<n;i++){
        cout <<num[i]<< "\n";
    }    
}
void input_num(){
  cin>>n;
  string a;
  for(int i =0;i<n;i++){
    cin>>a;
    num.push_back(a);
  }
  start();
}
int main() {
  input_num();
}