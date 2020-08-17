def squirrel(N):
    res = 1
    if N == 1 or N == 0:
        return 1
    else:
        for n in range(1, N+1):
            res = res * n
        res_str = str(res)
        return res_str[0]


