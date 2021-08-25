#include <iostream>
#include <string>
#include <vector>
#include<string.h> 
using namespace std;

string solution(string new_id) {
    string ans = "";    
    for(int i=0;i<new_id.length();i++){
        if(new_id[i]>='A' and new_id[i]<='Z') new_id[i]=tolower(new_id[i]);
        if((new_id[i]>='a' and new_id[i]<='z')||(new_id[i]>='0' and new_id[i]<='9')||(new_id[i]=='-')|| (new_id[i]=='_')|| (new_id[i]=='.')) {
            ans +=new_id[i];
            continue;
        }
    }
    while(ans.find("..")!= string::npos){
      ans.replace(ans.find(".."),2,".");
    }
    if(ans.length()>0 && ans[0]=='.') ans = ans.substr(1,ans.length()-1);
    if(ans.length()>0 && ans[ans.length()-1]=='.')ans = ans.substr(0,ans.length()-1);
    if(ans.length()==0) ans = "a";
    if(ans.length()>=16)ans.substr(0,15);
    if(ans[ans.length()-1]=='.')ans = ans.substr(0,ans.length()-1);
    while(ans.length()<=2){
        ans += ans[ans.length()-1];
    }
    return ans;
}

int main() {
  string new_id ="..A";
  cin>>new_id;
  solution(new_id);
}