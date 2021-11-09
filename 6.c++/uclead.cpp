#include <iostream>
using namespace std;

void lcm(int a,int b,int c){
  cout<<a*b/c;
}

int gcd(int a,int b){
  int c = a%b;
  if(c==0) {
    cout<<b<<"\n";
    return b;
  }
  return gcd(b,c);
}

int main() {
  int a = 30;
  int b = 72;
  int re = gcd(a,b);
  lcm(a,b,re);
} 