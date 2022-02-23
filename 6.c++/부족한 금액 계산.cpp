using namespace std;

//시간 복잡도 O(1)
long long solution(int price, int money, int count)
{
    long long  answer = 0;
    
    //처음과 끝을 더하고, count/2 만큼 곱해준다.
    long long p = price+price*count;
    long long totalMoney = p*(count/2);
    if(count%2==1) totalMoney += price*(count/2+1);
    if(money<totalMoney) answer = totalMoney - money;
    return answer;
}

//다른 풀이
long long solution1(int price, int money, int count)
{
    long long  answer = 0;
    
    //, count/2 만큼 곱해준다.
    long long totalMoney = 1LL*price*count*(count+1)/2;
    return answer;
}