#include <iostream>
#include <queue>
using namespace std;

void lru(){
  int num[10] = {1,3,4,2,6,3,2,6,8,3};
  queue<int> n;
  for(int i:num){
    queue<int> re;
    while(!n.empty()){
      if(n.front()!=i){
        re.push(n.front());
      }
      n.pop();
    }
    re.push(i);
    if(re.size()>3)re.pop();
    n = re;
  }
  while(!n.empty()){
    cout<<n.front()<<" ";
    n.pop();
  }
}
int main() {
  lru();
}