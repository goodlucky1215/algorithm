#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

struct edge { //정렬을 위한 구조체
    int idx, x, y;
};
vector<edge> node; //정렬을 위한 배열
bool sortNode(edge a, edge b){
    if(a.y == b.y) {
        return a.x < b.x;
    }
    else
        return a.y > b.y;
}

struct nodePut{
  int left=-1;
  int right=-1;
};

nodePut nodeput[10001];
map<int,pair<int,int>> m;
void nodeFind(int now, edge e){
   pair<int,int> nowpos = m[now];
    if(nowpos.first > e.x) { //왼쪽자식인 경우
        if(nodeput[now].left ==-1) { //왼쪽 자식 끝인 경우
            nodeput[now].left = e.idx; //왼쪽 자식에 붙이기
        }
        else nodeFind(nodeput[now].left, e); //재귀적으로 탐색
    }
    else { //오른쪽 자식인 경우
        if(nodeput[now].right ==-1) { //오른쪽 자식 끝인 경우
            nodeput[now].right = e.idx;
        }
        else nodeFind(nodeput[now].right, e);

    }
}

vector<vector<int>> answer(2);
void preOrder(int high){
    answer[0].push_back(high+1);
    if(nodeput[high].left!=-1) preOrder(nodeput[high].left);
    if(nodeput[high].right!=-1) preOrder(nodeput[high].right);
}
void postOrder(int high){
    if(nodeput[high].left!=-1) postOrder(nodeput[high].left);
    if(nodeput[high].right!=-1) postOrder(nodeput[high].right);
    answer[1].push_back(high+1);
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
    //x,y,노드번호를 구하고 / sort정렬을 한다.
    for(int i=0;i<nodeinfo.size();i++){
        node.push_back({i, nodeinfo[i][0], nodeinfo[i][1]}); //정렬을 위한 배열
        m[i] = {nodeinfo[i][0], nodeinfo[i][1]}; //각 노드 번호별 x, y좌표 map에 저장
    }
    sort(node.begin(),node.end(), sortNode);

    //자신의 밑에 번호고 오른쪽 왼쪽 구분을 해서 left와 right로 나눠서 담는다.
    for(int i=1;i<nodeinfo.size();i++){
        nodeFind(node[0].idx,node[i]);
    }

    //전위 순회, 후위 순회를 시작한다.
    preOrder(node[0].idx);
    postOrder(node[0].idx);
    return answer;
}
