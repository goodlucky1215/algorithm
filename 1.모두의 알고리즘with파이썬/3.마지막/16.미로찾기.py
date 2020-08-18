def find_m(m,a,z):
    start=[a]
    qu=[a]
    while qu:
        q=qu.pop(0)
        for i in m[q]:
            
    

maze={
    'a':['e'],
    'b':['c','f'],
    'c':['b','d'],
    'd':['c'],
    'e':['a','i'],
    'f':['b','g','j'],
    'g':['f','h'],
    'h':['g','l'],
    'i':['e','m'],
    'j':['k','f','n'],
    'k':['j','o'],
    'l':['h','p'],
    'm':['i','n'],
    'n':['m','j'],
    'o':['k'],
    'p':['l']
    }
