import sys

pre = 0
count = 0
result = []


# test function
def location_test(arr, cur_col, num):
    # 모든 column 검사
    for i in range(num):
        if i == cur_col:
            continue
        elif (arr[i] == arr[cur_col]) or cur_col - i == arr[cur_col] - arr[i] or cur_col - i == arr[i] - arr[cur_col]:
            return False
    return True


def go_next_level(arr, cur_col, num):
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

    for i in range(num):
        arr[cur_col] = i
        global pre
        pre = cur_col
        if location_test(arr, cur_col, num):
            go_next_level(arr, cur_col + 1, num)
            if pre > cur_col:
                arr[pre] = sys.maxsize
    return False


def csp(n):
    f = open(n + "_csp_output.txt", 'w')
    num = int(n)
    global pre
    global count
    pre = 0
    count = 0
    arr = [sys.maxsize for i in range(num)]
    go_next_level(arr, 0, num)
    if count == 0:
        f.write("There is no solution")
        print("csp result: There is no solution")
    if count > 0:
        print("csp result:", result)
        f.write(str(result))

