a, b, c = int(input()), int(input()), int(input())

if a >= b >= c:
    a, b, c = c, b, a
elif a >= b <= c:
    if a > c:
        a, b, c = b, c, a
    else:
        a, b, c = b, a, c
elif a <= b >= c:
    if a > c:
        a, b, c = c, a, b
    else:
        a, b, c = a, c, b
elif a <= b <= c:
    a, b, c = a, b, c

print(a, b, c)
