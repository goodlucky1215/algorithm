#include <iostream>
using namespace std;

void resul(string a,int lenA,int namuge,string result){
  int c=0;
  while(lenA>=0){
    c=(a[lenA--]-'0')+namuge;
    if(c>=10) {
      namuge=1;
      c-=10;
    }else namuge=0;
    result+=('0'+c);
  }
  if(namuge>0)result+='1';
  for(int i=result.length()-1;i>=0;i--){
    cout<<result[i];
  }
}

void start(){
  string a,b;
  cin>>a>>b;
  int lenA = a.length()-1;
  int lenB = b.length()-1;
  string result="";
  int namuge=0;
  int c=0;
  while(lenA>=0 and lenB>=0){
    c=(a[lenA--]-'0')+(b[lenB--]-'0')+namuge;
    if(c>=10) {
      namuge=1;
      c-=10;
    }else namuge=0;
    result+=(c+'0');
  }
  if(lenA>=0)resul(a,lenA,namuge,result);
  else resul(b,lenB,namuge,result);
}
int main() {
  start();
}