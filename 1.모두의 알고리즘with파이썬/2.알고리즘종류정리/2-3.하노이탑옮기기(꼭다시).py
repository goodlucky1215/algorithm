#하노이탑  ***어렵다***
def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:                             #원반 1개면 그냥 옮김.
        print('1번')
        print(from_pos,"->",to_pos)
        return

    hanoi(n-1,from_pos, aux_pos, to_pos) #원반n-1개를 중간 기둥에 이동시키고(그러니깐 n-1개에 대한 알고리즘을 한다고 생각하면 된다.)
    print(from_pos,"->",to_pos)          #가장 큰 원반을 마지막 기둥에 깐다
    print('2번')
    hanoi(n-1,aux_pos,to_pos,from_pos)   #이제 중간 기둥에 있던 n-1을 마지막 기둥에 이동시킨다.

print("n=1")
hanoi(1, 1, 3, 2)
print("n=2")
hanoi(2, 1, 3, 2)
print("n=3")
hanoi(3, 1, 3, 2)
