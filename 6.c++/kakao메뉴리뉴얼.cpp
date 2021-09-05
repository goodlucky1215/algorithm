#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

map<string,int> mapFood;
int courseArray[11];

void wordPut(string food,string foodAdd,int foodNumber,int foodPlusMenuSu){
    if(courseArray[foodPlusMenuSu]>=1){
        courseArray[foodPlusMenuSu] = max(courseArray[foodPlusMenuSu],++mapFood[foodAdd]);
    }
    for(int i=foodNumber;i<food.length();i++){
        wordPut(food,foodAdd+food[i],i+1,foodPlusMenuSu+1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    for(int i=0;i<course.size();i++){
        courseArray[course[i]]=1;
    }
    for(int j=0;j<orders.size();j++){
        sort(orders[j].begin(),orders[j].end());
        wordPut(orders[j],"",0,0);
    }
    for(int i=0;i<course.size();i++){
        if(courseArray[course[i]]>=2){
           for(auto iter = mapFood.begin(); iter!=mapFood.end();++iter){
                 if((iter->first).length()==course[i] && iter->second==courseArray[course[i]]){
                     answer.push_back(iter->first); 
                 }
            }
        }else continue;
    }
    sort(answer.begin(),answer.end());
    return answer;
}


int main() {
  vector<string> orders;
  vector<int> course;
  vector<string> solution(orders,course);
}