def fibonacci(n):
    a, b = 0, 1;
    while b <= n:
        a, b = b, a + b
        print(a, end = ' ')
    print()
fibonacci(1000)


def fibonacci(n):
    a, b = 0, 1;
    for _ in range(10):
        a, b = b, a + b
        print(a, end = ' ')
    print()
fibonacci(10)


def fibo(a, b, n, r):
    if b >= n:
        return r
    r.append(b)
    return fibo(b, a + b, n, r)
print(fibo(0, 1, 1000, r = []))

    
def fibo(a, b, n):
    if b >= n:
        return
    print(b, end = ' ')
    fibo(b, a + b, n)
    print()
fibo(0, 1, 1000)

    
def fibo1(n):
    if n <= 2:
        return 1
    else:
        return fibo1(n - 1) + fibo1(n - 2)

for x in range(1, 30 + 1):
    print(fibo1(x), end = ' ')
print()


def fibo2(a, b, n):
    if 0 >= n:
        return
    print(b, end = ' ')
    fibo2(b, a + b, n - 1)
    print()

fibo2(0, 1, 50)


def fibo3(a, b, n):
    if n <= 1:
        return b
    else:
        return fibo3(b, a + b, n - 1)

print(fibo3(0, 1, 100))


def fibonacci1(n):
    a, b = 0, 1;
    while n >= 1:
        a, b = b, a + b
        n -= 1
    return a
print(fibonacci1(10))

print(fibonacci1(1000))
