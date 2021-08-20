#include <iostream>
using namespace std;
string word;
//경우는 3가지뿐이다.
//문자가 전부 같아서 -1
//중간에 아예 다른 값이 있어서 전체 길이 word.lenght()
//팰리드롬이라서 한 글자만 빼주면 되는 word.length()-1
int start(int wordLen){
  bool oneWord = true;
  for(int i=0;i<wordLen/2;i++){
    if(word[i]!=word[wordLen-i-1]){
      return wordLen;
    }
    if(word[i]!=word[i+1]) oneWord = false;
  }
  if(!oneWord) return wordLen-1;
  else return -1; 
}
void input(){
  cin>>word;
  cout<<start(word.length());
}
int main() {
  input();
}