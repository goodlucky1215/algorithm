def solution(files):
    a='1234567890'
    He=[]
    for f,i in enumerate(files): 
        k=''
        for j in i:
            if j not in a:#숫자가 없다면 계속 넣어줌
                k+=j
            else:
                He.append([])#숫자가 있다면 리스트 만들고
                He[f].append(k)#파일 이름 넣어줌
                break
        k=''
        for j in i[len(He[f][0]):]:
            if j in a and len(k)<5:#숫자가 있고, 5개 이하면 넣어줌
                k+=j
            else:
                break
        He[f].append(k)#마지막에 숫자 넣은파일
    #파일 이름으로 정렬 후에, 숫자로 정렬 시켜서 리스트 불러
    answer=[files[i] for i in sorted(range(len(He)),key=lambda x:(He[x][0].lower(),int(He[x][1])))]

    return answer
print(solution(	["img12.png", "img10000", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
