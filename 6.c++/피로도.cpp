#include <string>
#include <vector>

using namespace std;

//시간 복잡도 O(n!) 
int result = 0;
void sun(int sizes,int k,vector<vector<int>> dungeons,int dunLen, bool check[],int re ){
    if(dunLen==sizes){
        result = max(result, re);
        return;
    }
    for(int i=0;i<dunLen;i++){
       if(check[i]==false){
         check[i] = true;
         if(dungeons[i][0]<=k)
         sun(sizes+1,k-dungeons[i][1],dungeons,dunLen,check,re+1);
         else sun(sizes+1,k,dungeons,dungeons.size(),check,re);
         check[i]=false;
       }
    }
}
int solution(int k, vector<vector<int>> dungeons) {
    
    bool check[8]={0,0,0,0,0,0,0,0};
    int p =k;
    sun(0,p,dungeons,dungeons.size(),check,0);
    return result;
}