#순차 탐색으로 특정 값의 위치 찾기
def search_list(a,x):
    for i in range(len(a)):
        if x==a[i]:
            return i
    return -1

v=[17,92,18,23,35,45,74,44]
print(search_list(v,45))
print(search_list(v,900))

#찾는 값의 모든 위치 찾기
def search_list(a,x):
    s=[]
    for i in range(len(a)):
        if x==a[i]:
            s.append(i)
    return s

v=[17,92,18,23,17,45,74,44,17]
print(search_list(v,17))
print(search_list(v,900))

#학생 번호가 주어졌을 때, 학생 이름 찾기
def search_stu(a,b,c):
    for i in range(len(a)):
        if a[i]==c:
            return b[i]
    return '?'

stu_num=[39,14,67,105]
stu_name=['justin','ariel','jinny','kein']
print(search_stu(stu_num,stu_name,67))
print(search_stu(stu_num,stu_name,100))
