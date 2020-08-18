def search_name(a,b,c): #a는 번호들,b는 찾는사람의 번호
    for i in range(len(a)):
        if a[i]==b:
            return c[i]
    return '?'

stu_no=[39,14,67,105]
stu_name=['justin','jonh','mike','summer']
print(search_name(stu_no,14,stu_name))
