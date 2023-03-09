from collections import deque
from time import perf_counter_ns

TIMES = 10_000
a_list = list(range(TIMES))
a_deque = deque(a_list)

def average_time(func, times):
    total = 0.0
    for _ in range(times):
        start = perf_counter_ns()
        func()
        total += perf_counter_ns() - start
    return total / times

list_time = average_time(lambda: a_list.pop(0), TIMES)
deque_time = average_time(lambda: a_deque.popleft(), TIMES)
gain = list_time / deque_time

print(f"list.pop(0)      {list_time:.6} ns")
print(f"deque.popleft() {deque_time:.6} ns  ({gain:.6}x faster)")