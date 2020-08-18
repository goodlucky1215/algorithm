h,b,c,s=map(int,input().split())
p=h*b*c*s
q=2**10
if p<8:
    print("%.1f bit" % p)
elif p/8<1024:
    print(" %.1f Byte" % (p/8))
elif p/8/q<1024:
    print("%.1f KB" % (p/8/q))
elif p/8/(q**2)<1024:
    print("%.1f MB" % (p/8/(q**2)))
elif p/8/(q**3)<1024:
    print("%.1f GB" % (p/8/(q**3)))
else:
    print("%.1f TB" % (p/8/(q**4)))
