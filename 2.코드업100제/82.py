a=int(input(),16)

for i in range(1,16):
    print(hex(a)[2:].upper()+'*'+hex(i)[2:].upper()+'='+'%x'.upper() % (a*i))
