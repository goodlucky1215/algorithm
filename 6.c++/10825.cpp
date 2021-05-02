#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct student{
  string person;
  int kor;
  int en;
  int math;
};
vector <student> stuRank;
int n;
bool sortRank(student stu1,student stu2){
  if(stu1.kor!=stu2.kor) return stu1.kor>stu2.kor;
  if(stu1.en!=stu2.en) return stu1.en<stu2.en;
  if(stu1.math!=stu2.math) return stu1.math>stu2.math;
  return stu1.person<stu2.person;
}
void result(){
  sort(stuRank.begin(),stuRank.end(),sortRank);
  for(int i=0;i<n;i++){
    cout<<stuRank[i].person<<"\n";
  }
}
void push_num(){
  cin>>n;
  for(int i=0;i<n;i++){
    student re;
    cin>>re.person>>re.kor>>re.en>>re.math;
    stuRank.push_back(re);
  }
  result();
}
int main() {
  push_num();
}