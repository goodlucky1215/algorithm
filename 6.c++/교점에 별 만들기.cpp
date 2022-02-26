#include <string>
#include <vector>

using namespace std;

//시간 복잡도 O(n^2+n) => O(n^2) 
// 백터랑 string 연속으로 글자 넣는 법 
// string temp(col, '.'); answer.assign(row, temp);
vector<string> solution(vector<vector<int>> line) {
    long long x,y;
    long long maxX = -10000000001;
    long long maxY = -10000000001;
    long long minX = 10000000001;
    long long minY = 10000000001;
    vector<pair<long long ,long long >> v;
    for(int i = 0;i<line.size()-1;i++){
        for(int j=i+1;j<line.size();j++){
            long long  bottom = (long long)line[i][0]*line[j][1]-line[i][1]*line[j][0];
            if(bottom==0) continue;
            long long  top1 = ((long long)line[i][1]*line[j][2]-(long long)line[i][2]*line[j][1]);
            long long  top2 = ((long long)line[i][2]*line[j][0]-(long long)line[i][0]*line[j][2]);
            if(top1%bottom!=0 or top2%bottom!=0) continue;
            x = (long long)top1/bottom;
            y = (long long)top2/bottom;
            maxX = max(x,maxX); 
            maxY = max(y,maxY);
            minX = min(x,minX); 
            minY = min(y,minY);
            v.push_back(make_pair(y,x));
        }
    }
    vector<string> answer;
    long long row = maxY-minY+1;
    long long col = maxX-minX+1;
    string temp(col, '.');
    answer.assign(row, temp);
    for(int i=0;i<v.size();i++){
        long long  x1,y1;
        y1= maxY-v[i].first;
        x1= v[i].second-minX;
        answer[y1][x1]='*';
    }
    return answer;
}