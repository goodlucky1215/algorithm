#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

bool answer = 0;
int sachic(int sSize,int N){
    int s = N;
    for(int i=0;i<sSize;i++){
        s=s*10+N;
    }
    return s;
}
int solution(int N, int number) {
    if(number==N) return 1;
    vector<unordered_set<int>> se(8);
    se[0].insert(N);
    for(int k=1;k<8;k++) {
        se[k].insert(sachic(k,N));
        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                if(i+j+1!=k) continue;
                for(int x:se[i]){
                    for(int y:se[j]){
                        se[k].insert(x+y);
                        int xy = x-y;
                        if(xy>0) se[k].insert(xy);
                        int xy1 = x/y;
                        if(xy1>0) se[k].insert(xy1);
                        se[k].insert(x*y);
                    }
                }
            }
        }
        if(se[k].find(number)!=se[k].end()) return k+1;
    }
    return -1;
}