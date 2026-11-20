import copy
import sys
import time
rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7
print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}
print(stops[(13.0418, 80.2341)])
try:
    stops[[13.0418, 80.2341]] = "Chennai"
except TypeError as e:
    print("Error:", e)
a = [10, 20, 30]
b = a
b[0] = 100
print("Aliasing:", a)
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0][0] = 99
print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)
coordinates = [(10, 20), (30, 40), (50, 60)]
for x, y in coordinates:
    print("X:", x, "Y:", y)
def change_list(values):
    values[0] = 500
numbers = [1, 2, 3]
change_list(numbers)
print("Changed list:", numbers)
data = ([1, 2, 3], "Bus Stop")
data[0].append(4)
print("Tuple:", data)
values_list = list(range(1000000))
values_tuple = tuple(values_list)
print("List memory:", sys.getsizeof(values_list))
print("Tuple memory:", sys.getsizeof(values_tuple))
for name, constructor in [("List", list), ("Tuple", tuple)]:
    start = time.perf_counter()
    obj = constructor(range(1000000))
    creation = time.perf_counter() - start
    start = time.perf_counter()
    x = obj[500000]
    indexing = time.perf_counter() - start
    print(name, "Creation:", creation)
    print(name, "Indexing:", indexing)