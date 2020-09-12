def divide(p):
    if p =='':
        return ''
    opench=0
    close=0
    last=''

    for index in range(len(p)):
        if p[index]=='(':
            opench+=1
        else:
            close+=1
        last=p[index]
        if opench == close:
            if last ==')':
                return p[:index+1]+divide(p[index+1:])
            else:
                return reverse(p[:index+1],divide(p[index+1:]))

def reverse(u,v):
    empty='('
    empty+=v+')'
    for i in range(1,len(u)-1):
        if u[i] =='(':
            empty+=')'
        else:
            empty+='('
    return empty

def solution(p):

    return divide(p)
