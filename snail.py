# 달팽이 배열
'''
data = [[0] * 5 for i in range(5)]  # 0이 5행5열로 들어가 있는 2차원 리스트
n = 0;
s = 1;
i = 0;
j = -1;
k = 5

while True:
    for p in range(1, k + 1):
        n += 1
        j += s
        data[i][j] = n

    k -= 1
    if k <= 0:
        break
    for p in range(1, k + 1):
        n += 1
        i += s
        data[i][j] = n

    s *= -1

for i in range(len(data)):
    for j in range(len(data[0])):
        print('%3d ' % data[i][j], end='')
    print()
'''

# 배열 달팽이
# Start
# 단 1이 입력되면 종료
# 배열의 선언
while True:
    num = int(input("Enter Num: "))
    if num == 1:
        break

    A1313 = [[0 for col in range(num + 1)] for row in range(num + 1)]  # 6*6배열

    k = 0
    sw = 1
    i = 1
    j = 0
    n = num

    while True:
        for p in range(1, n + 1):
            k = k + 1
            j = j + sw
            A1313[i][j] = k
        n = n - 1
        if n > 0:
            for p in range(1, n + 1):
                k = k + 1
                i = i + sw
                A1313[i][j] = k
            sw = sw * (-1)
        else:
            break

    for a in range(1, num + 1):
        for b in range(1, num + 1):
            print("%3d" % A1313[a][b], end=" ")
        print(' ')