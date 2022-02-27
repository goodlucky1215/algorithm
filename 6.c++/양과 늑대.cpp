#include <string>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> edgesVector(17);
int answer = 1;
void goSheep(int sheepSu, int wolfSu, int root,bool check[],queue<int> load,vector<int> info){
    answer = max(sheepSu,answer);
    for(int i=0;i<edgesVector[root].size();i++) {
        if(check[edgesVector[root][i]]==0) 
            load.push(edgesVector[root][i]);
    }
    int loadSize = load.size();
    for(int j =0;j<loadSize;j++){
        int i = load.front();
        load.pop();
        if(info[i]==1 and sheepSu>wolfSu+1){
            check[i] = 1;
            goSheep(sheepSu,wolfSu+1, i,check,load,info);
            check[i] = 0;
        }else if(info[i]==0){
            check[i] = 1;
            goSheep(sheepSu+1,wolfSu, i,check,load,info);
            check[i] = 0;
        }
        load.push(i);
    }
}

int solution(vector<int> info, vector<vector<int>> edges) {
    for(int i=0;i<edges.size();i++){
        edgesVector[edges[i][0]].push_back(edges[i][1]);
        edgesVector[edges[i][1]].push_back(edges[i][0]);
    }
    bool check[17]={0,};
    check[0]=1;
    queue<int> load;
    goSheep(1,0,0,check,load,info);
    return answer;
}