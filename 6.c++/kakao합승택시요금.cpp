#include <iostream>
#include <string>
#include <vector>

using namespace std;
int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 0;
    int load[201][201];
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(i==j)load[i][j]=0;
            else load[i][j]=11111111;
        }
    }
    for(int i=0;i<fares.size();i++){
        load[fares[i][0]][fares[i][1]]=fares[i][2];
        load[fares[i][1]][fares[i][0]]=fares[i][2];
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            for(int k=1;k<=n; k++){
                load[j][k] = min(load[j][k], load[j][i]+load[i][k]);
            } 
        }
    }
    answer = 1e9;
    for(int i=1;i<=n;i++){
         answer = min(answer,load[s][i]+load[i][a]+load[i][b]);   
    }
    return answer;
}
int main() {
  vector<vector<int>> fares = {{4, 1, 10}, {3, 5, 24}, {5, 6, 2}, {3, 1, 41}, {5, 1, 24}, {4, 6, 50}, {2, 4, 66}, {2, 3, 22}, {1, 6, 25}};
  solution(6,4,6,2,fares);
}