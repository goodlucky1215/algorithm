#include <string>
#include <vector>
#include <queue>
#include <math.h>
using namespace std;

//시간 복잡도 O(n^2+n) => O(n^2)
int solution(int n, vector<vector<int>> wires) {
    int network[101][101] = {0,};
    for(int i=0;i<wires.size();i++){
        network[wires[i][0]][wires[i][1]] = 1;
        network[wires[i][1]][wires[i][0]] = 1;
    }
    int answer = 101;
    for(int i=0;i<wires.size();i++){
        int start = wires[i][0];
        int end = wires[i][1];
        bool check[101] = {0,};
        check[start] = 1;
        queue<int> qu;
        qu.push(start);
        int t = 0;
        while(!qu.empty()){
            t++;
            int first = qu.front();
            qu.pop();
            for(int i=1;i<end;i++){
                if(network[first][i]==1 and check[i]==0) {
                    qu.push(i); 
                    check[i] = 1;
                }
            }
            for(int i=end+1;i<=n;i++){
                if(network[first][i]==1 and check[i]==0) {
                    qu.push(i);
                    check[i] = 1;
                }
            }
        }
        answer = min(answer,abs(n-2*t));
    }
    return answer;
}