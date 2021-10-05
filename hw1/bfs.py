def goal(arr, num):
    true = 1
    for i in range(num - 1):
        for j in range(i + 1, num, 1):
            # check if in same row
            if arr[i] == arr[j]:
                true = 0
            # check if in left up
            if (arr[i] - arr[j]) == i - j:
                true = 0
            # check if in left down
            if (arr[i] - arr[j]) == (j - i):
                true = 0
    if true == 0:
        return False
    else:
        return True


def bfs(n):
    print("Bfs")
    f = open(n + "_bfs_output.txt", 'w')
    num = int(n)
    arr = []
    queue = [arr]
    a = 0

    while True:
        if len(queue) == 0 and a != 0:
            print("There is no solution")
        test = queue.pop(0)
        a = 1
        if len(test) < num:
            for j in range(num):
                new = test[:]
                new.append(j)
                queue.append(new)
        else:
            if goal(test, num):
                for i in range(num):
                    test[i] += 1
                f.write(str(test))
                break
    f.close()
