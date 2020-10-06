n=int(input())
s=list(map(int,input().split()))
st=[]
for i in range(1,n+1):
    st.append(i)
    st.insert(i-s[i-1]-1,i)
    st.pop()
print(*st)
    
