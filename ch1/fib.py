from functools import lru_cache
from typing import Generator

memo = {0:0, 1:1, 2:1}

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)

def fibmemo(n: int) -> int:
    if n not in memo:
        memo[n] = fibmemo(n-2) + fibmemo(n-1)
    return memo[n]

@lru_cache(maxsize=None)
def fiblru(n: int) -> int:
    if n < 2:
        return n
    return fiblru(n-2) + fiblru(n-1)

def fibiter(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
    return next

def fibiter_gen(n: int) -> Generator[int, None, None]:
    print(f"first time n is {n}")
    yield 0
    if n > 0:
        print("seconds")
        yield 1
    
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        print('in loop')
        yield next

#challenge question: Implement a fib implentation of your own design, use unit testing to 
#compare against other implementations


if __name__ == "__main__":

    print(fib2(11))
    print(fibmemo(50))
    print(fiblru(50))
    print(fibiter(50))

    for i in fibiter_gen(2):
        print(i)