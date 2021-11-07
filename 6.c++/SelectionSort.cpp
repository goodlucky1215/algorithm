#include <iostream>
using namespace std;
int num[10] = {10,9,11,7,2,3,1,5,45,44};
// 속도는 O(n^2) 공간은 O(n)
void selectionSort(){
  for(int i=0;i<10;i++){
    int me = i;
    for(int j=i+1;j<10;j++){
      if(num[me]>num[j]) me = j;
    }
    int su = num[i];
    num[i] = num[me];
    num[me] = su;
  }
}

void result(){
  for(int i=0;i<10;i++){
    cout<<num[i]<<" ";
  }
}
int main() {
  selectionSort();
  result();
} 