import random
import sys


def get_score(arr, num):
    score = 0
    for i in range(num - 1):
        for j in range(i + 1, num, 1):
            # check if in same row
            if arr[i] == arr[j]:
                score += 1
            # check if in left up
            if (arr[i] - arr[j]) == i - j:
                score += 1
            # check if in left down
            if (arr[i] - arr[j]) == (j - i):
                score += 1
    return score


# 한 col 내부에서 다른 row로 이동할 떄 점수 계산 => 한 col score (최소 값, 해당 row) return
def calculate_score(arr, col, num):
    score = [sys.maxsize for i in range(num)]
    min_score = sys.maxsize
    min_row = -1
    for i in range(num):
        tem = arr[:]
        # 같은 row일 경우 판단하지 않음
        if i == arr[col]:
            continue
        tem[col] = i
        score[i] = get_score(tem, num)
        if min_score >= score[i]:
            if min_score == score[i]:
                min_row = int(random.choice([min_row, i]))
            else:
                min_row = i
                min_score = score[i]
    return min_score, min_row


# num개의 열 중에서 최소 비교, 선택 후 해당 col, row, 점수 return
def h(arr, num):
    each_score = [sys.maxsize for i in range(num)]
    each_min_row = [sys.maxsize for i in range(num)]
    min_score = sys.maxsize
    min_col = sys.maxsize
    # 이때, i는 col, col끼리 min비교, 최소 score를 가지는 col선택
    for i in range(num):
        score, min_row = calculate_score(arr, i, num)
        each_score[i] = score
        each_min_row[i] = min_row
        if min_score >= each_score[i]:
            if min_score == each_score[i]:
                min_col = int(random.choice([min_col, i]))
            else:
                min_col = i
                min_score = each_score[i]
    min_row = each_min_row[min_col]
    return min_score, min_col, min_row


# 총 함수. arr 설정하고 답을 구하는 과정. 최소 score가 0이라면 정답.
def hc(n):
    num = int(n)
    f = open(n + "_hc_output.txt", 'w')
    arr = [random.randrange(0, num) for i in range(num)]
    pre_score = sys.maxsize
    count = 0

    while True:
        score, col, row = h(arr, num)
        if count > 1000:
            print(n, "hc result: There is no solution or too many restart")
            f.write("no solution")
            break
        if score == 0:
            arr[col] = row
            for i in range(num):
                arr[i] += 1
                if i == num - 1:
                    f.write(str(arr[i]))
                else:
                    f.write(str(arr[i]))
                    f.write(" ")
            print("hc result: ", arr)
            break
        elif score > 0:
            if pre_score <= score:
                count += 1
                arr = [random.randrange(0, num) for i in range(num)]
                pre_score = sys.maxsize
            elif pre_score > score:
                pre_score = score
                arr[col] = row
    f.close()
