import sys

input = sys.stdin.readline
s, p = map(int, input().split())
dna = input().strip()
alpha = list(map(int, input().split()))  # {‘A’, ‘C’, ‘G’, ‘T’}
make_dna = [0, 0, 0, 0]
# 처음 p 갯수를 만든다.
for i in dna[:p]:
    if i == 'A': make_dna[0] += 1
    elif i == 'C': make_dna[1] += 1
    elif i == 'G': make_dna[2] += 1
    elif i == 'T': make_dna[3] += 1

#체크 메서드
def check():
    for i in range(4):
        if alpha[i] > make_dna[i]:
            return 0
    return 1

# 처음 적합한지 체크한다.
result = check()

# 나머지도 확인한다.
index = 0
for i in dna[p:]:
    if i == 'A':
        make_dna[0] += 1
    elif i == 'C':
        make_dna[1] += 1
    elif i == 'G':
        make_dna[2] += 1
    elif i == 'T':
        make_dna[3] += 1

    if dna[index] == 'A':
        make_dna[0] -= 1
    elif dna[index] == 'C':
        make_dna[1] -= 1
    elif dna[index] == 'G':
        make_dna[2] -= 1
    elif dna[index] == 'T':
        make_dna[3] -= 1
    index += 1
    result += check()
print(result)