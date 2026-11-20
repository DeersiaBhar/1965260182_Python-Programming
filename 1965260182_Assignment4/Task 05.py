import random
import time
import sys
readings = [4, 7, 12, 55, -60, 0, 3]
valid1 = []
fahrenheit1 = []
for c in readings:
    if -50 <= c <= 50:
        valid1.append(c)
        fahrenheit1.append(c * 9/5 + 32)
valid2 = [
    c for c in readings
    if -50 <= c <= 50
]
fahrenheit2 = [
    c * 9/5 + 32 for c in valid2
]
valid3 = list(
    filter(lambda c: -50 <= c <= 50, readings)
)
fahrenheit3 = list(
    map(lambda c: c * 9/5 + 32, valid3)
)
alarms = [
    i for i, c in enumerate(readings)
    if -50 <= c <= 50 and not (2 <= c <= 8)
]
print("Loop:", valid1, fahrenheit1)
print("Comprehension:", valid2, fahrenheit2)
print("Map and filter:", valid3, fahrenheit3)
print("Alarm minutes:", alarms)
temperature_dict = {
    i: c for i, c in enumerate(readings)
    if -50 <= c <= 50
}
print("Dictionary:", temperature_dict)
temperature_set = {
    c for c in readings
    if -50 <= c <= 50
}
print("Set:", temperature_set)
my_list = [x for x in range(1000)]
my_generator = (x for x in range(1000))
print("List memory:", sys.getsizeof(my_list))
print("Generator memory:", sys.getsizeof(my_generator))
for n in [10000, 100000, 1000000]:
    data = [random.randint(-60, 60) for _ in range(n)]
    start = time.perf_counter()
    result1 = [x for x in data if -50 <= x <= 50]
    t1 = time.perf_counter()-start
    start = time.perf_counter()
    result2 = list(filter(lambda x: -50 <= x <= 50, data))
    t2 = time.perf_counter()-start
    print(n, "Comprehension:", t1, "Filter:", t2)
    assert result1 == result2