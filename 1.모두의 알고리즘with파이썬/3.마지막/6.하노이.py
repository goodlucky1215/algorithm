#하노이
def hanoi(n,from_pos,to_pos,aux_pos):
    if n==1:
        print(from_pos,"->",to_pos)
        return
    
    hanoi(n-1,from_pos,aux_pos,to_pos) #n-1의 원반을 중간 지점에 옮긴다.
    print(from_pos,"->",to_pos)        #제일 큰 원반을 가장 끝에 옮긴다. 
    hanoi(n-1,aux_pos,to_pos,from_pos)
    
print("n=1")
hanoi(1,1,3,2)
print("n=2")
hanoi(2,1,3,2)
print("n=3")
hanoi(3,1,3,2)
