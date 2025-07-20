# towers of hanoi solver

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: list[T] = []
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:

    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)

def main():
    num_discs = 25
    twr_a: Stack[int] = Stack()
    twr_b: Stack[int] = Stack()
    twr_c: Stack[int] = Stack()

    for i in range(1, num_discs+1):
        twr_a.push(i)
    print(twr_a)
    print(twr_b)
    print(twr_c)

    hanoi(twr_a, twr_c, twr_b, num_discs)
    print(twr_a)
    print(twr_b)
    print(twr_c)

if __name__ == "__main__":
    main()

