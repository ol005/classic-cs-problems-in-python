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
    
    def get_list(self) -> list[T]:
        return self._container

    def __len__(self) -> int:
        return len(self._container)
    
    def peek(self) -> T:
        return self._container[-1]
    
    def __repr__(self) -> str:
        return repr(self._container)

def print_towers(towers: list[Stack[int]], n: int) -> None:
    print('******************')
    for i in range(n-1, -1, -1):
        for twr in towers:
            li = twr.get_list()
            if len(li) > i:
                print(f'| {li[i]} |', end='')
            else:
                print('|   |', end='')
        print('')
    print('******************')

# 1.7 challenge exercise question 3
# implement iter solution for tower of hanoi and variable number of towers

# odd goes left, even discs move right
def hanoi_iter(towers: list[Stack[int]], discs: int, num_towers: int) -> None:
    smallest_move: bool = True
    end: Stack[int] = towers[-1]
    small_loci: int = 0
    direction: int = 1 if discs % 2 == 0 else -1

    #end condition:
    while(len(end) < discs):
        print_towers(towers, discs)
        if(smallest_move):
            #move smallest disc left if total is odd, right if total is even, looping
            towers[(small_loci + direction) % len(towers)].push(towers[small_loci].pop())
            small_loci = (small_loci + direction) % len(towers)
        else:
            for i in range(0, num_towers):
                if i == small_loci or len(towers[i]) == 0:
                    continue
                for j in range(0, num_towers):
                    if i != j and (len(towers[j])==0 or towers[i].peek() < towers[j].peek()): #found the one valid move
                        towers[j].push(towers[i].pop())
                        break
                else:
                    continue
                break
        smallest_move = not smallest_move
    print_towers(towers, discs)    

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:

    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


def main():
    num_discs: int = 8
    num_towers: int = 3
    towers: list[Stack[int]] = []
    for i in range(num_towers):
        towers.append(Stack())


    for i in range(num_discs, 0, -1):
        towers[0].push(i)

    #hanoi(twr_a, twr_c, twr_b, num_discs)
    hanoi_iter(towers, num_discs, num_towers)

if __name__ == "__main__":
    main()

