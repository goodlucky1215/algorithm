def find_key(box,n) : #시작점, n은 갯수
    if n==0:
        return [[]]
    s = []
    for i in range(len(box)):
        for j in find_key(box[i+1:],n-1):
            s.append([box[i]]+j)
    return s

def find_mini(col,answer) : #컬럼번호, 컬럼set
    s = []
    for i in range(1,len(col)+1):
        s=find_key(col,i)
        for j in s:
            if tuple(j) in answer:
                return False
    return True

def find_unique(col,relation) : #컬럼번호, 컬럼값
    len_col = len(relation)
    answer = set()
    for i in range(len_col):
        value = []
        for j in col:
            value.append(relation[i][j])
        if tuple(value) in answer:
            return False
        answer.add(tuple(value))
    return len_col==len(answer)

def solution(relation):
    answer = set()
    re_len = len(relation[0])
    box = []
    for i in range(re_len) : box.append(i)
    for i in range(1,re_len+1) :
        s = find_key(box,i)
        for j in s:
            if find_mini(j,answer) : #최소성고려
                if find_unique(j,relation) : #유일성고려
                    answer.add(tuple(j))
    return len(answer)