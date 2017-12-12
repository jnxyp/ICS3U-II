
def f_stupid(n:int):
    if n <= 1:
        return 1
    else:
        return n * f_stupid(n-1)


def f(n: int):
    r = 1
    for i in range(2, n + 1): r *= i
    return r


def fr(n: int): return n * fr(n - 1) if n > 1 else 1




print(f(6))
print(fr(6))
print(f_stupid(6))
