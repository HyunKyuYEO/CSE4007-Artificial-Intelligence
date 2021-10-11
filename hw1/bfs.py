def goal(arr, num):
    for i in range(num - 1):
        for j in range(i + 1, num, 1):
            # check if in same row
            if arr[i] == arr[j]:
                return False
            # check if in left up
            if (arr[i] - arr[j]) == i - j:
                return False
            # check if in left down
            if (arr[i] - arr[j]) == (j - i):
                return False
    return True


# queue 이용하여 bfs. child node(next column)으로 가능한 모든 row값들을 queue에 넣은다음 진행
def bfs(n):
    f = open(n + "_bfs_output.txt", 'w')
    num = int(n)
    arr = []
    queue = [arr]
    count = 0

    while True:
        count += 1
        if len(queue) == 0:
            print(n, "bfs result: There is no solution")
            f.write("no solution")
            break
        test = queue.pop(0)
        if len(test) < num:
            for j in range(num):
                new = test[:]
                new.append(j)
                queue.append(new)
        else:
            if goal(test, num):
                for i in range(num):
                    test[i] += 1
                    if i == num - 1:
                        f.write(str(test[i]))
                    else:
                        f.write(str(test[i]))
                        f.write(" ")
                print("bfs result:", test)
                break
        if count > 100000:
            print("too many iteration")
            f.write("cannot find solution, too many iteration")
            break
    f.close()
