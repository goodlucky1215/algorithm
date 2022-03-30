#include <string>
#include <set>
#include <queue>
#include <vector>


using namespace std;


int solution(int n, vector<vector<int>> results) {

    vector<set<int>> winVec(n+1);

    vector<set<int>> loseVec(n+1);

    for(int i=0;i<results.size();i++){

          winVec[results[i][0]].insert(results[i][1]);

          loseVec[results[i][1]].insert(results[i][0]);

    }

    for(int i=1;i<=n;i++){

         bool check[101] = {0,};

         queue<int> qu;

          for(int j : winVec[i]){

             qu.push(j);

             check[j] = 1;

          }

          while(!qu.empty()){

              int k = qu.front();

              qu.pop();

              for(int j:winVec[k]){

                    if(check[j]==0){

                        check[j]=1;

                         winVec[i].insert(j);

                         loseVec[j].insert(i);

                         qu.push(j);

                    }

             }

      }

    }

    int answer = 0;

    int n1 = n-1;

    for(int i=1;i<=n;i++){

          if(winVec[i].size()+loseVec[i].size() ==n1) answer++;

   }

    return answer;
}