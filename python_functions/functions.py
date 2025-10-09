def func():
    tot = 0
    for i in range(1, 10001):
        tot += i
    print(tot)

n = int(input())
for i in range(n):
    func()