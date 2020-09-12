def find(time,b,c):
    f1,f2=divmod(time,len(b))#시간에 따른 음악 길이 계산
    b=b*f1+b[:f2] #몫은 곱해주고 나머지는 일부까지만틀어서 저장
    if c in b:#악보(b)안에 음(c)가 있다면 Ture
        return True
    else:
        return False
def solution(m, musicinfos):
    m=m.replace('C#','c')#두글자인 것은 한글자로 다 치환
    m=m.replace('D#','d')
    m=m.replace('F#','f')
    m=m.replace('G#','g')
    m=m.replace('A#','a')
    answer = ''#정답
    time=0#재생시간 넣기 위해서
    for i in range(len(musicinfos)):
        musicinfos[i]=musicinfos[i].split(',')#문단 나누기
        musicinfos[i][3]=musicinfos[i][3].replace('C#','c')#두글자인 것은 한글자로 다 치환
        musicinfos[i][3]=musicinfos[i][3].replace('D#','d')
        musicinfos[i][3]=musicinfos[i][3].replace('F#','f')
        musicinfos[i][3]=musicinfos[i][3].replace('G#','g')
        musicinfos[i][3]=musicinfos[i][3].replace('A#','a')
        a=musicinfos[i][0].split(':')
        b=musicinfos[i][1].split(':')
        #곡 길이 계산해서 넣어줌
        musicinfos[i][0]=(int(b[0])-int(a[0]))*60+(int(b[1])-int(a[1]))
        if find(musicinfos[i][0],musicinfos[i][3],m): 
            if time<musicinfos[i][0]:#둘 다 true일때 재생시간이 긴 곡을 넣어줌
                time=musicinfos[i][0]#재생시간 저장
                answer=musicinfos[i][2]#곡 제목 저장
    if answer=='':
        answer='(None)'#모든 곡에 전부 없다면 반
    return answer
