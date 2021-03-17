a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

if a >= b >= c:
    m, n = b, c
elif a >= b <= c and a >= c:
    m, n = b, c
elif a >= b <= c and a <= c:
    m, n = b, a
elif a <= b >= c:
    m, n = a, c
elif a <= b <= c:
    m, n = a, b

if (m <= d and n <= e) or (m <= e and n <= d):
    print("YES")
else:
    print("NO")
