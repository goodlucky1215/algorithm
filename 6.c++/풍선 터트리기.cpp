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