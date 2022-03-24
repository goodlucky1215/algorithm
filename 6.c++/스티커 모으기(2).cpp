#include <iostream>

#include <vector>

using namespace std;

int solution(vector<int> sticker){
    int stickerSize = sticker.size();
    if(stickerSize==1) return sticker[0];
    else if(stickerSize==2) return max(sticker[0],sticker[1]);    
    else if(stickerSize==3){
        int a = max(sticker[0],sticker[1]);
        a = max(a,sticker[2]);
        return a;
    }
    int s[100001] = {0,};
    s[0]=sticker[0];
    s[1]=sticker[1];
    s[2]=sticker[2]+sticker[0];
    for(int i=3;i<stickerSize-1;i++){
            s[i]=sticker[i]+max(s[i-3],s[i-2]);
    }
    int s1[100001] = {0,};
    s1[1]=sticker[1];
    s1[2]=sticker[2];
    s1[3]=sticker[3]+sticker[1];
    for(int i=4;i<stickerSize;i++){
            s1[i]=sticker[i]+max(s1[i-3],s1[i-2]);
    }
    return max(max(s[stickerSize-3],s[stickerSize-2]),max(s1[stickerSize-2],s1[stickerSize-1]));

}