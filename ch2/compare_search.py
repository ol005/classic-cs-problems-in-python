# chapter 2 challenge questions:

#question 1 - compare linear vs binary search

import time
import random
from typing import Callable
from generic_search import linear_contains, binary_contains

NUM_TESTS = 10000
MAX_NUM = 1000000

def test_int_search(nums: list[int], i: int, searchf: Callable[[list[int], int], bool]) -> int:
    t0: float = time.perf_counter_ns()
    searchf(nums, i)
    t1: float = time.perf_counter_ns() 
    return (t1-t0)

def main() -> None:
    nums: list[int] = [i for i in range(0, MAX_NUM)]
    t_linear: int = 0
    t_binary: int = 0
    for _ in range(0, NUM_TESTS):
        #test linear and binary search over 10000 random numbers
        #include possible testing input for not found
        val = random.randint(0, MAX_NUM * 3)
        t_linear += test_int_search(nums, val, linear_contains)
        t_binary += test_int_search(nums, val, binary_contains)

    print(f"linear: {(t_linear / NUM_TESTS) / 1_000_000}")
    print(f"binary: {(t_binary / NUM_TESTS) / 1_000_000}")
if __name__ == '__main__':
    main()