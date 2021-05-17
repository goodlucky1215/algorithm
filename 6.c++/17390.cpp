#include <iostream>
#include <algorithm>
using namespace std;
int q,number[300001];
void start(){
  int a,b;
  for(int i=0;i<q;i++){
    cin>>a>>b;
    cout<<number[b]-number[a-1]<<"\n";
  }
}
void push_num(){
  int numSu;
  cin>>numSu>>q;
  for(int i=1;i<=numSu;i++){
    cin>>number[i];
  }
  sort(number,number+numSu+1);
  for(int i=2;i<=numSu;i++){
    number[i]+=number[i-1];
  }
  start();
}
int main() {
  push_num();
}