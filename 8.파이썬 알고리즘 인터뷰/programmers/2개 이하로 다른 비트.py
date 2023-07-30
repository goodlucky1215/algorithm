def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)  # 짝수일 경우 +1만 하면 된다.
        else:
            number_bin = '0' + bin(i)[2:]
            number_bin = number_bin[:number_bin.rindex('0')] + '10' + number_bin[number_bin.rindex('0') + 2:]
            answer.append(int(number_bin, 2))

    return answer