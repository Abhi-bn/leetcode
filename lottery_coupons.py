def func(number):

    # dic = {k: 0 for k in range(1, )}
    dic = {}
    for i in range(1, number + 1):
        s = str(i)
        sum = 0
        for k in range(len(s)):
            sum += int(s[k])
        dic.setdefault(sum, 0)
        dic[sum] += 1
    mx = max(dic, key=dic.get)
    print(mx)
    c = 0
    for k, v in dic.items():
        if v == dic[mx]:
            c += 1
    return c


print(func(101))
