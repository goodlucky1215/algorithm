def solution(n, arr1, arr2):
    answer = []
    c='0'+str(n)+'b'
    for i in range(n):
        answer.append('')
        arr1[i]=format(arr1[i],c)
        arr2[i]=format(arr2[i],c)
        for j in range(n):
            if arr1[i][j]=='0' and arr2[i][j]=='0':
                answer[i]+=' '
            else:
                answer[i]+='#'
    return answer
