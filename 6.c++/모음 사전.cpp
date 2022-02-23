#include <string>
#include <vector>
#include <math.h>
using namespace std;
//시간 복잡도 O(n^3)
int solution(string word) {
    //각 자리수 갯수
    int place[6];
    //나올 수 있는 모든 경우의 수
    int total = 0; 
    for(int i=1;i<6;i++){
        place[i] = pow(5,i);
        total+=place[i];
    }
    //n자리수가 나오는 간격
    for(int i=1;i<6;i++){
        place[i] = total/place[i];
    }
    int answer = 0;
    for(int i=0;i<word.length();i++){
        if(word[i]=='A') answer+=1;
        else if(word[i]=='E') answer+=place[i+1]*1+1;
        else if(word[i]=='I') answer+=place[i+1]*2+1;
        else if(word[i]=='O') answer+=place[i+1]*3+1;
        else if(word[i]=='U') answer+=place[i+1]*4+1;
    }
    return answer;
}


//시간 복잡도 O(n)
//규칙을 찾아야 한다!!  'A', 'E', 'I', 'O', 'U'
//1자리 수라면,  'A' -> 'E' -> 'I' -> 'O' -> 'U'  1씩증가
//2자리 수라면,  'A'ㅁ -> 'E'ㅁ -> 'I'ㅁ -> 'O'ㅁ -> 'U'ㅁ 6씩 차이(AA가 1번째라면 EA는 7번째)
//3자리 수라면, 6*5+1 = 31개씩 차이
//4자리 수라면, 31*5+1 = 156개씩 차이
//5자리 수라면, 156*5+1 = 781씩 차이
int solution1(string word) {
    //각 자리수 갯수 차이
    int place[5] = {781,156,31,6,1};
    //나올 수 있는 모든 경우의 수
    int answer = 0;
    for(int i=0;i<word.length();i++){
        if(word[i]=='A') answer+=1;
        else if(word[i]=='E') answer+=place[i]*1+1;
        else if(word[i]=='I') answer+=place[i]*2+1;
        else if(word[i]=='O') answer+=place[i]*3+1;
        else if(word[i]=='U') answer+=place[i]*4+1;
    }
    return answer;
}