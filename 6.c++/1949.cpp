#include <iostream>
#include <vector>
using namespace std;

int people[10001][2];
bool check[10001];
vector<vector<int>> vec(10001);

void goodVillage(int village){
 check[village] = true;
 for(int i:vec[village]){
   if(!check[i]){
     goodVillage(i);

     people[village][0] += max(people[i][0], people[i][1]);
     people[village][1] += people[i][0];
  }
 }
}
void start(){
 int n;
 cin>>n;
 for(int i=1;i<=n;i++){
  cin>>people[i][1];
 }
 
 for(int i=1;i<n;i++){
  int a,b;
  cin>>a>>b;
  vec[a].push_back(b);
  vec[b].push_back(a);
 }

 goodVillage(1);

 cout<<max(people[1][0],people[1][1]);
}

int main(){
 start();
}