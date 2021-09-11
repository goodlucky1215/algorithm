#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <sstream>
#include <cstring>
#include <algorithm>
using namespace std;
vector<int> split(string in){
    vector<int> result;
    stringstream ss(in);
    string temp;
    
    while(getline(ss,temp,' ')){
        if(temp=="cpp")result.push_back(0);
        else if(temp=="java")result.push_back(1);
        else if(temp=="python")result.push_back(2);
        break;
    }
    
    while(getline(ss,temp,' ')){
        if(temp=="backend")result.push_back(0);
        else if(temp=="frontend")result.push_back(1);      
        break;
    }
    
    while(getline(ss,temp,' ')){
        if(temp=="junior")result.push_back(0);
        else if(temp=="senior")result.push_back(1);     
        break;
    }
    
    while(getline(ss,temp,' ')){
        if(temp=="chicken")result.push_back(0);
        else if(temp=="pizza")result.push_back(1);     
        break;
    }
    
    while(getline(ss,temp,' ')){
        result.push_back(stoi(temp));
        break;
    }
    return result;
}

void sortAll(vector <int> personInfo[3][2][2][2]){
    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++){
            for(int k=0;k<2;k++){
                for(int t=0;t<2;t++){
                    sort(personInfo[i][j][k][t].begin(),personInfo[i][j][k][t].end());
                }
            }
        }
    }
}

vector<int> qSplit(string in){
    vector<int> result;
    stringstream ss(in);
    string temp;
    
    while(getline(ss,temp,' ')){
        if(temp=="cpp")result.push_back(0);
        else if(temp=="java")result.push_back(1);
        else if(temp=="python")result.push_back(2);
        else result.push_back(3);
        break;
    }
    
    while(getline(ss,temp,' ')){
        if(temp=="and") continue;
        if(temp=="backend")result.push_back(0);
        else if(temp=="frontend")result.push_back(1);
        else result.push_back(2);
        break;
    }
    
    while(getline(ss,temp,' ')){
        if(temp=="and") continue;
        if(temp=="junior")result.push_back(0);
        else if(temp=="senior")result.push_back(1);
        else result.push_back(2);
        break;
    }
    
    while(getline(ss,temp,' ')){
        if(temp=="and") continue;
        if(temp=="chicken")result.push_back(0);
        else if(temp=="pizza")result.push_back(1);
        else result.push_back(2);
        break;
    }
    
    while(getline(ss,temp,' ')){
        result.push_back(stoi(temp));
        break;
    }
    
    return result;
}

int findPerson(vector<int> querySplit,vector <int> personInfo[3][2][2][2]){
    int cnt = 0;
    int i1,j1,k1,t1;
    if(querySplit[0]==3) i1 =0,querySplit[0]--;
    else i1 = querySplit[0];
    if(querySplit[1]==2) j1 =0,querySplit[1]--;
    else j1 = querySplit[1];
    if(querySplit[2]==2) k1 =0,querySplit[2]--;
    else k1 = querySplit[2];
    if(querySplit[3]==2) t1 =0,querySplit[3]--;
    else t1 = querySplit[3];
    for(int i=i1;i<=querySplit[0];i++){
        for(int j=j1;j<=querySplit[1];j++){
            for(int k=k1;k<=querySplit[2];k++){
                for(int t=t1;t<=querySplit[3];t++){
                    int size = personInfo[i][j][k][t].size();
                    int sizeIdx = lower_bound(personInfo[i][j][k][t].begin(),personInfo[i][j][k][t].end(),querySplit[4])-personInfo[i][j][k][t].begin();
                    cnt+=size-sizeIdx;
                }
            }
        }
    }
    return cnt;
}

vector<int> solution(vector<string> info, vector<string> query) {
    //언어, 지원 직군, 경력구분, 소울푸드
    vector <int> personInfo[3][2][2][2];
    for(int i=0;i<info.size();i++){
        vector<int> result = split(info[i]);
        personInfo[result[0]][result[1]][result[2]][result[3]].push_back(result[4]);
    }
    sortAll(personInfo);
    
    vector<int> answer;
    vector<int> querySplit;
    for(int i=0;i<query.size();i++){
        querySplit = qSplit(query[i]);
        answer.push_back(findPerson(querySplit,personInfo));

    }
    return answer;
}
int main() {
  std::cout << "Hello World!\n";
}