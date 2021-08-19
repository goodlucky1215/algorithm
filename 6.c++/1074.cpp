#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;
int N;
int i, j;
int result;

void start(int x,int y,int n){
  if(x == i && y == j){
    cout<<result;
    exit(0);
  }
  if(i<=x+n-1&&j<=y+n-1){
    ;
  }
  else {
    result += n*n;
    return;
  }

  start(x,y,n/2);
  start(x,y+n/2,n/2);
  start(x+n/2,y,n/2);
  start(x+n/2,y+n/2,n/2);
}

int main() {
    scanf("%d", &N);
    scanf("%d %d", &i, &j);
    start(0, 0, 1<<N);
}