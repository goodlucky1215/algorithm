#include <iostream>
using namespace std;
void binarySearch(int num[],int target){
  int left=0;
  int right=9;
  while(left<=right){
    int mid = (left+right)/2;
    if(num[mid]<target) left=mid+1;
    else if(num[mid]>target) right=mid-1;
    else {
      cout<<mid;
      break;
    }
  }

}
int main() {
  int num[10] = {1,2,3,4,5,6,7,8,9,10};
  binarySearch(num,10);
  
} 