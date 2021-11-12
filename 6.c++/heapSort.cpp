#include <iostream>
using namespace std;

void heapify(int n,int i,int heap[])//n은 힙길이, i는 부모노드
{ 
  int node = i;
	int left = 2 * i+1;//왼쪽, 오른쪽 할 아이
  int right =  2 * i+2;
//조건1) 만약 힙길이(n)보다 작거나 같다면 오른쪽에 있는 것은 이미 지정된 값이라는 거임. 
//조건2) 왼쪽과 오른쪽을 비교해서 오른쪽값이 더 크다면 부모랑 오른쪽이랑 비교
//왼쪽 값이 더 크다면 왼쪽값과 부모랑 비교

	if(left < n && heap[node] < heap[left]) node = left;
	if(right < n && heap[node] < heap[right]) node = right;
//왼쪽 6
	if(i != node)
	{
		swap(heap[i],heap[node]);
		heapify(n,node,heap);
	}
}

void heapSort(int arr[]){
  int arrLen = 7;
  	for(int i = (arrLen/2)-1; i >= 0; i--){
	  	heapify(arrLen,i,arr);
    }

    for(int i = arrLen-1; i >= 0; i--){
      swap(arr[0],arr[i]);
      heapify(i,0,arr);
    }

}
int main() {
  int arr[7] = {230, 10, 60, 550, 40, 220, 20};
  heapSort(arr);
  for(int i:arr)cout<<i<<" ";
} 