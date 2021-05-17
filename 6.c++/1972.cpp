#include <iostream>
#include <set>
using namespace std;
void surpriseFind(string word){
  int wordLen = word.size();
  for(int i=1;i<wordLen;i++){
    set <string> wordAll;
    for(int j=0;j<wordLen-i;j++){
      string word1 = "";
      word1+=word[j];
      word1+=word[j+i];
      if(wordAll.find(word1)==wordAll.end()) wordAll.insert(word1);
      else {
        cout<<word<<" is NOT surprising."<<"\n";
        return;
      }
    }
  }
  cout<<word<<" is surprising."<<"\n";
}
void start(){
  string word;
  while(1){
    cin>>word;
    if(word=="*") break;
    else surpriseFind(word);
  }
}
int main() {
  start();
}