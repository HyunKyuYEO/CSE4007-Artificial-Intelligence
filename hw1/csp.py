import sys

# 조건 만족 따지기 위한 전역변수
pre = 0
count = 0
result = []


# 현재 후보군으로 포함된 column까지 적절한지 검사해주는 함수.
def location_test(arr, cur_col):
    # 현재까지 column 검사
    for i in range(cur_col):
        if arr[i] == arr[cur_col]:
            return False
        if cur_col - i == arr[cur_col] - arr[i]:
            return False
        if cur_col - i == arr[i] - arr[cur_col]:
            return False
    return True


# 재귀적으로 호출, 다음 column 붙이기 위해서 호출됨
def go_next_level(arr, cur_col, num):
    # 모든 column 다 붙었을 경우, count == 1이면 정답, 나머지는 필요 없음
    if cur_col == num:
        global count
        count += 1
        if count > 1:
            return False
        for i in range(num):
            arr[i] += 1
            global result
            result = arr[:]
        return True
    # 모든 column 붙지 못했을 때 재귀적으로 붙여줌.
    for i in range(num):
        arr[cur_col] = i
        global pre
        pre = cur_col
        if location_test(arr, cur_col):
            go_next_level(arr, cur_col + 1, num)
            if pre > cur_col:
                arr[pre] = sys.maxsize
    return False


def csp(n):
    f = open(n + "_csp_output.txt", 'w')
    num = int(n)
    global count
    count = 0
    arr = [sys.maxsize for i in range(num)]
    go_next_level(arr, 0, num)
    if count == 0:
        f.write("There is no solution")
        print("csp result: There is no solution")
    if count > 0:
        print("csp result:", result)
        f.write(str(result))
