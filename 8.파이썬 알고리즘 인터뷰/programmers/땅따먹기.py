def solution(land):
    land_row = len(land)
    land_col = len(land[0])

    for i in range(land_row - 1):
        for j in range(land_col):
            land[i + 1][j] = max([land[i][k] + land[i + 1][j] for k in range(land_col) if j != k])

    return max(land[land_row - 1])