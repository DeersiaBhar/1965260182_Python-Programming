import random
import time
import sys

readings = [2, 3.5, 9, 55, -60, 7, 1, 4]

# Method 1: For loop with append
def using_loop(data):
    valid = []
    fahrenheit = []
    alarms = []

    for minute, c in enumerate(data):
        if -50 <= c <= 50:
            valid.append(c)
            fahrenheit.append(c * 9/5 + 32)

            if c < 2 or c > 8:
                alarms.append(minute)

    return valid, fahrenheit, alarms

# Method 2: List comprehension
def using_comprehension(data):
    valid = [c for c in data if -50 <= c <= 50]

    fahrenheit = [
        c * 9/5 + 32
        for c in data if -50 <= c <= 50
    ]

    alarms = [
        i for i, c in enumerate(data)
        if -50 <= c <= 50 and (c < 2 or c > 8)
    ]

    return valid, fahrenheit, alarms

# Method 3: Map and filter
def using_map_filter(data):
    valid = list(filter(
        lambda c: -50 <= c <= 50, data
    ))

    fahrenheit = list(map(
        lambda c: c * 9/5 + 32, valid
    ))

    alarms = [
        i for i, c in enumerate(data)
        if -50 <= c <= 50 and (c < 2 or c > 8)
    ]

    return valid, fahrenheit, alarms

print("Loop:", using_loop(readings))
print("Comprehension:", using_comprehension(readings))
print("Map and filter:", using_map_filter(readings))

print("All results same:",
      using_loop(readings) ==
      using_comprehension(readings) ==
      using_map_filter(readings))

# Dictionary comprehension
temperature_dict = {
    i: c for i, c in enumerate(readings)
    if -50 <= c <= 50
}

print("Dictionary:", temperature_dict)

# Set comprehension
temperature_set = {
    c for c in readings if -50 <= c <= 50
}

print("Set:", temperature_set)

# Performance testing
for n in [10000, 100000, 1000000]:

    data = [
        random.uniform(-60, 60)
        for _ in range(n)
    ]

    start = time.perf_counter()
    a = using_loop(data)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    b = using_comprehension(data)
    t2 = time.perf_counter() - start

    start = time.perf_counter()
    c = using_map_filter(data)
    t3 = time.perf_counter() - start

    print("\nReadings:", n)
    print("Loop:", t1)
    print("Comprehension:", t2)
    print("Map/filter:", t3)
    print("Same results:", a == b == c)

# Memory comparison
list_data = [x for x in readings if -50 <= x <= 50]

generator_data = (
    x for x in readings if -50 <= x <= 50
)

print("\nList memory:", sys.getsizeof(list_data))
print("Generator memory:", sys.getsizeof(generator_data))

# Special tests
print("All valid:", using_loop([2, 3, 4]))
print("All invalid:", using_loop([100, -100]))