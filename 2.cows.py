n = int(input())

if n >= 11 and n <= 14:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print(n, 'korovy')
else:
    print(n, 'korov')

# 1 21 31 41 51 = korova
#
# 2 3 4 22 23 24 = korovy
#
# 5 - 20 25 - 30 = korov
