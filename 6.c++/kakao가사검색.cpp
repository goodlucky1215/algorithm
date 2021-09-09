#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int resultValue(string wo,vector<string> wordsAll[10001]){
    int quSize = wo.find_first_of('?');
    int io=0,hi=0;
    for(int i=quSize;i<wo.length();i++){
        wo[i]='a';
    }
    
    io = lower_bound(wordsAll[wo.length()].begin(),wordsAll[wo.length()].end(),wo)-wordsAll[wo.length()].begin();
    
    for(int i=quSize;i<wo.length();i++){
        wo[i]='z';
    }
  
    hi = lower_bound(wordsAll[wo.length()].begin(),wordsAll[wo.length()].end(),wo)-wordsAll[wo.length()].begin();

    return (hi-io);
}

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    vector<string> wordsAll[10001];
    vector<string> wordsAllRe[10001];
    for(int i=0;i<words.size();i++){
        wordsAll[words[i].length()].push_back(words[i]);
        reverse(words[i].begin(),words[i].end());
        wordsAllRe[words[i].length()].push_back(words[i]);
    }
    for(int i=0;i<10001;i++){
        sort(wordsAll[i].begin(),wordsAll[i].end());
        sort(wordsAllRe[i].begin(),wordsAllRe[i].end());
    }
    for(int i=0;i<queries.size();i++){
        int cnt = 0;
        if(queries[i][0]=='?')  {
            reverse(queries[i].begin(),queries[i].end());
            cnt = resultValue(queries[i],wordsAllRe);
        }
        else {
            cnt = resultValue(queries[i],wordsAll);
        }
        answer.push_back(cnt);
    }
    return answer;
}

int main() {
string wo = "sf?dsf?";
int quSize = wo.find_first_of('?');
cout<<quSize;
  std::cout << "Hello World!\n";
}

