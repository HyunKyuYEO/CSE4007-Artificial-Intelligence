def make_plane(n):
    arr = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(0)
        arr.append(tmp)
    return arr
