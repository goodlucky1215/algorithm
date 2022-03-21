#include <string>
#include <vector>
#include <sstream>
#include <set>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer(2,0);
    multiset<int> se;
    string a;
    int b;
    for(int i=0;i<operations.size();i++){
        stringstream ss;
        ss.str(operations[i]);
        ss>>a>>b;
        if(a=="I") se.insert(b);
        else if(a=="D" and !se.empty()){
            if(b==1) se.erase(--se.end());           
            else se.erase(se.begin());
        }
    }
    
    if(!se.empty()){
        set<int>::iterator iter = se.begin();
        answer[1] = *iter;
        iter = --se.end();
        answer[0] = *iter;
    }
    return answer;
}