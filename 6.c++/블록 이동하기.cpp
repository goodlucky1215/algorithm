#include <string>
#include<queue>
#include <vector>


using namespace std;

int xy[4] = {1,-1,1,-1};

int xy2[2][4] = {{1,1,-1,-1},{1,1,-1,-1}};

int answer = 10000000;

int n;


bool checkLoad(int x, int y, int x1, int y1,vector<vector<int>> board){

  if(x>=0 and x<=n and y>=0 and y<=n and x1>=0 and x1<=n and y1>=0 and y1<=n and board[x][y]==0 and board[x1][y1]==0) return true;

  return false;

}


struct load{

  int x1, y1, x2, y2;

  int re;

  int shape;

};


load loadPut(int x, int y,int x2,int y2,int re,int sh){

                    load lo1;

                    lo1.x1=x; lo1.y1=y;

                    lo1.x2=x2; lo1.x2=y2;

                    lo1.re=re; lo1.shape=sh;

                    return lo1;

}


int solution(vector<vector<int>> board) {

    n = board.size()-1;

    bool check[100][100][100][100];

    for(int i=0;i<=n;i++)

        for(int j=0;j<=n;j++)

            for(int k=0;k<=n;k++)

                for(int t=0;t<=n;t++)check[i][j][k][t]=0;

    queue<load> qu;

    check[0][0][0][1] = 1;

    load lo;

    lo.x1=0; lo.y1=0; lo.x2=0; lo.y2=1;

    lo.re=0;lo.shape=1;

     qu.push(lo);

    while(!qu.empty()){

            load lo = qu.front();

            qu.pop();


            if(answer<=lo.re) continue;

            if((lo.x1==n and lo.y1==n) or (lo.x2==n and lo.y2==n)) {

        answer = min(answer,lo.re);

        continue;

    }

            lo.re++;

            if(lo.shape==1) {

                    for(int i=0;i<2;i++){

                    int x3 = lo.x1+xy[i];

                    int y3 = lo.y1+xy2[0][i];

              if(checkLoad(x3,y3,x3,lo.y1,board)) {

                if(xy[i]==1 and check[lo.x2][lo.y2][x3][y3]==0) {

                    check[lo.x2][lo.y2][x3][y3]=1;

                    load lo1;

                    lo1.x1=lo.x2; lo1.y1=lo.y2;

                    lo1.x2=x3; lo1.x2=y3;

                    lo1.re=lo.re; lo1.shape=2;

                    qu.push(lo1);

                }

                else if(check[x3][y3][lo.x2][lo.y2]==0){

                    check[x3][y3][lo.x2][lo.y2]=1;

                    load lo1;

                    lo1.x1=x3; lo1.y1=y3;

                    lo1.x2=lo.x2; lo1.x2=lo.y2;

                    lo1.re=lo.re; lo1.shape=2;

                    qu.push(lo1);

                   }

            }

        }

        for(int i=2;i<4;i++){

            int x3 =lo.x2+xy[i];

            int y3 =lo.y2+xy2[0][i];

            if(checkLoad(x3,y3,x3,lo.y2,board)) {

                if(xy[i]==1 and check[lo.x1][lo.y1][x3][y3]==0){

                    check[lo.x1][lo.y1][x3][y3]=1;

                    load lo1;

                    lo1.x1=lo.x1; lo1.y1=lo.y1;

                    lo1.x2=x3; lo1.x2=y3;

                    lo1.re=lo.re; lo1.shape=2;

                    qu.push(lo1);

                }

                else if(check[x3][y3][lo.x1][lo.y1]==0){

                    check[x3][y3][lo.x1][lo.y1]=1;

                    load lo1;

                    lo1.x1=x3; lo1.y1=y3;

                    lo1.x2=lo.x1; lo1.x2=lo.y1;

                    lo1.re=lo.re; lo1.shape=2;

                    qu.push(lo1);

                }


            }


        }


      

      if(lo.x1+1<=n and lo.x2+1<=n and board[lo.x1+1][lo.y1] ==0 and board[lo.x2+1][lo.y2] ==0 and check[lo.x1+1][lo.y1][lo.x2+1][lo.y2]==0) {

           check[lo.x1+1][lo.y1][lo.x2+1][lo.y2]=1;

            qu.push(loadPut(lo.x1+1,lo.y1,lo.x2+1,lo.y2,lo.re,1));

        }

        if(lo.x1-1>=0 and lo.x2-1>=0 and board[lo.x1-1][lo.y1] ==0 and board[lo.x2-1][lo.y2] ==0 and check[lo.x1-1][lo.y1][lo.x2-1][lo.y2]==0) {

            check[lo.x1-1][lo.y1][lo.x2-1][lo.y2]=1;

qu.push(loadPut(lo.x1-1,lo.y1,lo.x2-1,lo.y2,lo.re,1));

        }

      if(lo.y2+1<=n and board[lo.x2][lo.y2+1]==0 and check[lo.x2][lo.y2][lo.x2][lo.y2+1]==0) {

          check[lo.x2][lo.y2][lo.x2][lo.y2+1]=1;

qu.push(loadPut(lo.x2,lo.y2,lo.x2,lo.y2+1,lo.re,1));

      }

        if(lo.y1-1>=0 and board[lo.x1][lo.y1-1]==0 and check[lo.x1][lo.y1-1][lo.x1][lo.y1]==0) {


         check[lo.x1][lo.y1-1][lo.x1][lo.y1]=1; 

qu.push(loadPut(lo.x1,lo.y1-1,lo.x1,lo.y1,lo.re,1));


      }

    }///lo.shape==1

    else {

        if(lo.y1+1<=n and lo.y2+1<=n and board[lo.x1][lo.y1+1] ==0 and board[lo.x2][lo.y2+1] ==0 and check[lo.x1][lo.y1+1][lo.x2][lo.y2+1]==0) {

            check[lo.x1][lo.y1+1][lo.x2][lo.y2+1]=1;          qu.push(loadPut(lo.x1,lo.y1+1,lo.x2,lo.y2+1,lo.re,2));

        }

       if(lo.y1-1>=0 and lo.y2-1>=0 and board[lo.x1][lo.y1-1] ==0 and board[lo.x2][lo.y2-1] ==0 and check[lo.x1][lo.y1-1][lo.x2][lo.y2-1]==0) {

check[lo.x1][lo.y1-1][lo.x2][lo.y2-1]=1;

qu.push(loadPut(lo.x1,lo.y1-1,lo.x2,lo.y2-1,lo.re,2));

        }

       if(lo.x2+1<=n and board[lo.x2+1][lo.y2]==0 and check[lo.x2][lo.y2][lo.x2+1][lo.y2]==0) {

           check[lo.x2][lo.y2][lo.x2+1][lo.y2]=1;

qu.push(loadPut(lo.x2,lo.y2,lo.x2+1,lo.y2,lo.re,2));

       }

      

       if(lo.x1-1>=0 and board[lo.x1-1][lo.y1]==0 and check[lo.x1-1][lo.y1][lo.x1][lo.y1]==0) {


           check[lo.x1-1][lo.y1][lo.x1][lo.y1]=1;

qu.push(loadPut(lo.x1,lo.y1,lo.x1,lo.y1-1,lo.re,2));


       }

        for(int i=0;i<2;i++){

            int x3 = lo.x1+xy2[1][i];

            int y3 = lo.y1+xy[i];

            if(checkLoad(x3,y3,lo.x1,y3,board)) {

                if(xy[i]==1 and check[lo.x2][lo.y2][x3][y3]==0){

                    check[lo.x2][lo.y2][x3][y3]=1;

                    qu.push(loadPut(lo.x2,lo.y2,x3,y3,lo.re,1));

                }

                else if(check[x3][y3][lo.x2][lo.y2]==0){

                    check[x3][y3][lo.x2][lo.y2]=1;       qu.push(loadPut(x3,y3,lo.x2,lo.y2,lo.re,1));

                }

            }

        }

        for(int i=2;i<4;i++){

            int x3 =lo.x2+xy2[1][i];

            int y3 =lo.y2+xy[i];

            if(checkLoad(x3,y3,lo.x2,y3,board)) {

                if(xy[i]==1 and check[lo.x1][lo.y1][x3][y3]==0) {

                    check[lo.x1][lo.y1][x3][y3]=1;

qu.push(loadPut(lo.x1,lo.y1,x3,y3,lo.re,1));

                }

                else if(check[x3][y3][lo.x1][lo.y1]==0){

                    check[x3][y3][lo.x1][lo.y1]=1;

                    qu.push(loadPut(x3,y3,lo.x1,lo.y1,lo.re,1));

                }


            }


        }

   }


}

    return answer;
}