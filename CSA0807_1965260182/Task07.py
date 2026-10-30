import time
def original(parts):
    result = ""
    for item in parts:
        result += item + ";"
    return result
def redesigned(parts):
    return ";".join(parts) + ";"
sizes = [1000, 10000, 200000]
for n in sizes:
    items = [f"Item{i}:Rs{i % 50}" for i in range(n)]
    start = time.perf_counter()
    old_result = original(items)
    old_time = time.perf_counter() - start
    start = time.perf_counter()
    new_result = redesigned(items)
    new_time = time.perf_counter() - start
    print("\nNumber of items:", n)
    print("Same output:", old_result == new_result)
    print("Original time:", old_time)
    print("Redesigned time:", new_time)
    if new_time > 0:
        print("Speed improvement:", old_time / new_time)