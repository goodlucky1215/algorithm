#include <string>
#include <vector>

using namespace std;

vector<vector<int>> cardWhere(7);
bool checkCard[7] = {0,};
int cardSu = 0;
int answer = 100000;

int countCtrl1(int a,int b,int y,vector<vector<int>> board,bool check[]){
    int count = 0;
    for(int i=a+1;i<b;i++){
        int num = board[i][y];
        if(num!=0 and check[num]==0){
            count++;
        }
    }
    return count++;
}

int countCtrl2(int a,int b,int x,vector<vector<int>> board,bool check[]){
    int count = 0;
    for(int i=a+1;i<b;i++){
        int num = board[x][i];
        if(num!=0 and check[num]==0){
            count++;
        }
    }
    return count++;
}

int countX(int a,int b,int y,vector<vector<int>> board,bool check[],int t){
    int numX = 0;
    int count = 0;
    if(t==1){
        for(int i=a+1;i<b;i++){
            int num = board[i][y];
            if(num!=0 and check[num]==0){
                numX = num;
                break;
            }
        }  
        count = numX - a + 1;
    }else{
         for(int i=a-1;i>=0;i--){
            int num = board[i][y];
            if(num!=0 and check[num]==0){
                numX = num;
                break;
            }
        }     
        count = a - numX + 1;
    }
    return count+1;
}

int countY(int a,int b,int x,vector<vector<int>> board,bool check[],int t){
    int numY = 0;
    int count = 0;
    if(t==1){
        for(int i=a+1;i<b;i++){
            int num = board[x][i];
            if(num!=0 and check[num]==0){
                numY = num;
                break;
            }
        }  
        count = numY - a;
    }else{
         for(int i=a-1;i>=0;i--){
            int num = board[x][i];
            if(num!=0 and check[num]==0){
                numY = num;
                break;
            }
        }
        count = a - numY; 
    }

    return count+1;
}

int cardChoiceSu(int r, int c,int x,int y,vector<vector<int>> board,bool check[7]){
    if(r==x and c==y) return 1;
    //ctrl키로 한 번에 가더라도 그 사이에 다른 카드를 만날 수도 있다.
    if(r!=x and c==y){
        if(r<x) return countCtrl1(r,x,y,board,check)+2;
        return countCtrl1(x,r,y,board,check)+2;
    }
    else if(r==x and c!=y){
        if(c<y) return countCtrl2(c,y,x,board,check)+2;
        return countCtrl2(y,c,x,board,check)+2;   
    }
    if(r!=x and c!=y) {
        //행 => 열 
        int xy = 0;
        if(r<x) {
            xy=countCtrl1(r,x,c,board,check);
            // 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동
            if(xy==0 and check[board[x][c]]!=0){
                xy= min(countX(x,4,c,board,check,1),x-r);
            }
        }
        else {
            xy =countCtrl1(x,r,c,board,check);
            if(xy==0 and check[board[x][c]]!=0){
                xy= min(countX(x,0,c,board,check,-1),r-x);                
            }
        }
        if(c<y) xy+=countCtrl2(c,y,x,board,check);
        else xy+=countCtrl2(y,c,x,board,check);   
        //열 => 행
        int yx = 0;
        if(c<y) {
            yx=countCtrl2(c,y,r,board,check);
            if(yx==0 and check[board[r][y]]!=0){
                yx= min(countY(y,4,r,board,check,1),y-c);         
            }
        }
        else {
            yx=countCtrl2(y,c,r,board,check);
            if(yx==0 and check[board[r][y]]!=0){
                yx= min(countY(y,0,r,board,check,-1),c-y);         
            }
        }
        if(r<x) yx+=countCtrl1(r,x,y,board,check);
        else yx +=countCtrl1(x,r,y,board,check);
        return min(xy,yx)+3;
    }
}
void goGame(vector<vector<int>> board, int r, int c, int re,int su,bool check[7]){
    if(su==cardSu){
        answer = min(answer,re);
    }
    for(int i=0;i<7;i++){
        if(checkCard[i]==0) continue;
        if(check[i] == 1) continue;
        check[i]=1;
        int x1 = cardWhere[i][0];
        int y1 = cardWhere[i][1];
        int x2 = cardWhere[i][2];
        int y2 = cardWhere[i][3];
        //1번 카드 갔다가 => 2번 카드
        int go12 = 0;
        go12 += cardChoiceSu(r,c,x1,y1,board,check);
        go12 += cardChoiceSu(x1,y1,x2,y2,board,check);
        goGame(board, x2, y2,re+go12,su+1,check);
        //2번 카드 갔다가 => 1번 카드
        int go21 = 0;
        go21 += cardChoiceSu(r,c,x2,y2,board,check);
        go21 += cardChoiceSu(x2,y2,x1,y1,board,check);
        goGame(board, x1, y1,re+go21,su+1,check);
        check[i]=0;
    }
}

int solution(vector<vector<int>> board, int r, int c) {
    bool check[7] = {0,};
    check[0]=1;
    //1. 카드의 위치를 다 모은다.
    for(int i = 0;i<4;i++){
        for(int j=0;j<4;j++){
            int num = board[i][j];
            if(num!=0){
                cardWhere[num].push_back(i);
                cardWhere[num].push_back(j);
                checkCard[num] = 1;
                cardSu++;
            }
        }
    }
    cardSu/=2;
    //2. 갯수가 적으니깐 브루트포스로 다 돌아본다. => 최대 720 경우의 수
    goGame(board,r,c,0,0,check);
    return answer;
}