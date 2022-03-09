#include <string>
#include <vector>
#include <queue>
using namespace std;

//시간 복잡도 O(V+E)
//정점의 개수 : V(n), 간선의 갯수 E(edge.size())
int solution(int n, vector<vector<int>> edge) {
    vector<vector<int>> vec(n+1);
    bool check[20001] ={0,};
    check[1] = 1;
    // 노드들을 저장
    for(int i=0;i<edge.size();i++){
        int x = edge[i][0];
        int y = edge[i][1];
        vec[x].push_back(y);
        vec[y].push_back(x);
    }
    int nodeSu = 1; //최소 간선
    int answer = vec[1].size(); //최소 간선에 따른 갯수
    // 최소 간선들에 대한 값 담기
    queue<pair<int,int>> qu;
    for(int i=0;i<vec[1].size();i++){
        qu.push(make_pair(vec[1][i],1));
        check[vec[1][i]] = 1;
    }
    while(!qu.empty()){
        int nodeNum = qu.front().first; //노드 번호
        int su = qu.front().second+1; //다음 간선 수
        qu.pop();
        int t = 0;
        //아직 방문하지않은 노드가 있다면 넣기
        for(int i=0;i<vec[nodeNum].size();i++){
            if(!check[vec[nodeNum][i]]){
                check[vec[nodeNum][i]]=1;
                qu.push(make_pair(vec[nodeNum][i],su));
                t++;
            }
        }
        //넣은 간선이 있고, 그 간선 수가 현재 간선 수보다 크다면 교체, 같다면 갯수 더하기
        if(t>0){
            if(su>nodeSu){
                nodeSu = su;
                answer = t;
            }
            else if(su==nodeSu) answer+=t;
        }
    }
    return answer;
}