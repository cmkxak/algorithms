def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    # 가로와 세로를 기준으로 각각 큰 값이 오도록 정렬
    max_w, max_h = max(sizes, key=lambda x: x[0]), max(sizes, key=lambda x: x[1])

    return max_w[0] * max_h[1]