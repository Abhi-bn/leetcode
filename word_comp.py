def func(k, s):
    a = []
    i = 0

    for i in range(len(s)):
        a.append(s[i])
        if i < k:
            continue
        temp = s[i]
        c = 0
        for l in range(len(a) - 1, len(a) - k - 1, -1):
            if a[l] == temp:
                c += 1

        if c == k:
            [a.pop() for i in range(k)]
    return a


print(func(3, 'abbcccb'))
