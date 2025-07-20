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

    yield 0
    if n > 0:
        yield 1
    
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        yield next

#challenge question: Implement a fib implentation of your own design, use unit testing to 
#compare against other implementations

def custom_fib(n : int) -> int:
    #combine memoization and iteration approach
    if memo.get(n) is not None:
        print("found with memo")
        return memo[n]
    
    ele_1 = memo.get(n-1, None)
    ele_2 = memo.get(n-2, None)
    if ele_1 is not None and ele_2 is not None:
        print("knows final 2")
        memo[n] = ele_1 + ele_2
        return memo[n]

    last, next = memo[0], memo[1] # guarteed to exist

    for i in range(n):
        if memo.get(i) is None:
            memo[i] = last
        last, next = next, last+next

    memo[n] = last
    return memo[n]


if __name__ == "__main__":

    #print(fib2(11))
    #print(fibmemo(50))
    #print(fiblru(50))
    #print(fibiter(50))

    print(custom_fib(50))
    print(custom_fib(40))
    print(custom_fib(51))
    print(memo)
    for i in fibiter_gen(51):
        print(i)