#include <string>

#include <vector>


using namespace std;


int solution(vector<vector<int>> triangle) {

    int answer = 0;

    int triangleSize = triangle.size()-1;

    for(int i=0;i<triangleSize;i++){

          int x = i+1;

          triangle[x][0]+=triangle[i][0];

          for(int j=1;j<x;j++){

                triangle [x][j]+= max(triangle[i][j-1],triangle[i][j]);

          }

          triangle[x][x] += triangle[i][i];

    }

    for(int i:triangle[triangleSize]) answer = max(answer,i);

    return answer;
}