#include <string>
#include <vector>

using namespace std;

int keyVecLen,lockLen;
int keyLen1;
int lockSu;
bool goKey(vector<pair<int,int>> keyVec,vector<vector<int>> lock){
    //왼쪽에서 오른쪽
    for(int k=0;k<lockLen+keyLen1-1;k++){
        //위에서 아래로
        for(int i=0;i<lockLen+keyLen1-1;i++){
            int t = 0;
            for(int j=0;j<keyVecLen;j++){
                int x = keyVec[j].first+i;
                int y = keyVec[j].second+k;
                if(x>=0 and y>=0 and x<lockLen and y<lockLen){
                    if(lock[x][y]==1) break;
                    else t++;
                }
            }
            if(t==lockSu) return true;
        }
    }
    return false;
}
bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    keyLen1 = key.size();
    int keyLen = key.size()-1;
    vector<pair<int,int>> keyVec;
    for(int i=0;i<=keyLen;i++){
        for(int j=0;j<=keyLen;j++){
            if(key[i][j]==1) keyVec.push_back(make_pair(i,j));
        }
    }
    lockLen = lock.size();
    for(int i=0;i<lockLen;i++){
        for(int j=0;j<lockLen;j++){
            if(lock[i][j]==0) lockSu++;
        }
    }
    keyVecLen = keyVec.size();
    //90도 돌리기.
    for(int i=0;i<4;i++){
        vector<pair<int,int>> keyVec1;
        for(int j=0;j<keyVecLen;j++){
            int x = keyVec[j].first;
            int y = keyVec[j].second;
            keyVec[j].first = y;
            keyVec[j].second = keyLen1-x;
            keyVec1.push_back(make_pair(keyVec[j].first-keyLen1,keyVec[j].second-keyLen1));
        }
        if(goKey(keyVec1,lock)) return true;
    }
    return false;
}