from fib import custom_fib, fibiter, fiblru
from time import perf_counter
from typing import Callable
# test custom implementation of fib in fib.py
memo = {0:0, 1:1, 2:1}

def test_accuracy(n: int, val: int) -> bool:
    correct_val: int = fibiter(n)
    return correct_val == val

def test_performance(n: int, func: Callable[[int], int]) -> tuple[float, float]:
    t1_start: float = perf_counter()
    func(n)
    t1_end: float = perf_counter()
    return t1_start, t1_end

def benchmark_comparison(n: int) -> None:
    func_to_test: list[Callable[[int], int]] = [fibiter, fiblru, custom_fib]
    for func in func_to_test:
        a: float
        b: float
        a, b = test_performance(n, func)
        print(f"function {func} took {b-a} seconds")

def main() -> None:
    print(test_accuracy(10, custom_fib(10)))
    print(test_accuracy(25, custom_fib(25)))
    print(test_accuracy(20, custom_fib(20)))
    benchmark_comparison(1000)
    benchmark_comparison(1000)
if __name__ == "__main__":
    main()