#include <string>
#include <vector>

using namespace std;

int solution(vector<int> a) {
    int aSize = a.size();
    if(aSize<3) return aSize;
    int left[aSize];
    left[0] = a[0];
    int right[aSize];
    right[aSize-1] = a[aSize-1];
    for(int i=1,j=aSize-2;i<aSize;i++,j--){
        left[i] = min(a[i],left[i-1]);
        right[j] = min(a[j],right[j+1]); 
    }
    int answer = 2;
    for(int i=1;i<aSize-1;i++){
        if((a[i]>=left[i-1] and a[i]<=right[i+1]) or 
           (a[i]<=left[i-1] and a[i]>=right[i+1]) or
           (a[i]<=left[i-1] and a[i]<=right[i+1])) answer++;
    }
    return answer;
}

/////////////////////////////////////////////////다른 풀이법/////////////////////////////

#include <string>
#include <vector>
#include <set>
using namespace std;

int solution(vector<int> a) {
    int aSize = a.size();
    if(aSize<3) return aSize;
    set<int> se;
    int frontNum = a[0];
    int backNum = a[aSize-1];
    se.insert(frontNum);
    se.insert(backNum);
    for(int i=1,j=aSize-2;i<aSize;i++,j--){
        if(frontNum>a[i]) {
            frontNum = a[i];
            se.insert(frontNum);
        }
        if(backNum>a[j]){
            backNum = a[j];
            se.insert(backNum);
        }
    }
    return se.size();
}