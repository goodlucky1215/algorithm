#순차 탐색: 리스트 안에 원소를 하나씩 순차적으로 비교하고 탐색
#찾는 값의 위치를 결과 값으로, 없다면 -1을 결과 값으로.
def search_list(a,x):
    n = len(a)
    for i in range(0,n):
        if x == a[i]:
            return i

    return -1

v=[17,92,18,33,58,7,33,42]
print(search_list(v,33))
print(search_list(v,900))

#7-1 리스트의 찾는 값의 모든 위치를 결과로 돌려준다. 없다면 []로 결과값.
def search_list(a,x):
    n = len(a)
    result=[]
    for i in range(0,n):
        if x == a[i]:
            result.append(i)
        
    return result

v=[17,92,18,33,58,7,33,42,33]
print(search_list(v,33))
print(search_list(v,900))

#학생 번호를 입력하면 번호에 해당하는 학생이름을 결과로. 없다면 ?으로 결과값.
def find_student(a,b,x):
    n=len(a)
    for i in range(n):
        if a[i]==x:
            return b[i]
    return '?'

stu_no=[39,24,36,105]
stu_name=['justin','john','mike','summer']
print(find_student(stu_no,stu_name,24))
print(find_student(stu_no,stu_name,345))
