#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    string num[10] = {"ze","on","tw","th","fo","fi","si","se","ei","ni"};
    int    numLen[10] = {2,1,1,3,2,2,1,3,3,2};
    string su = "";
    int answer = 0;
    for(int i=0;i<s.length();i++){
        if('0'<=s[i]and s[i]<='9'){
            answer*=10;
            answer+=(s[i]-'0');
        }else{
            su=s[i];
            su+=s[++i];
            for(int j=0;j<10;j++){
                if(num[j]==su){
                    answer*=10;
                    answer+=j;
                    i+=numLen[j];
                    break;
                }
            }
        }
    }
    return answer;
}