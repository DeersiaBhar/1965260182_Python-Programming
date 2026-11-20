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
a = [[1, 2], [3, 4]]
b = a
print("Aliasing:", a is b)
c = copy.copy(a)
d = a[:]
e = copy.deepcopy(a)
a[0][0] = 100
print("Original:", a)
print("Shallow:", c)
print("Deep:", e)
t = ([10, 20], "Chennai")
t[0].append(30)
print("Tuple with list:", t)
my_list = list(range(1000000))
my_tuple = tuple(range(1000000))
print("List memory:", sys.getsizeof(my_list))
print("Tuple memory:", sys.getsizeof(my_tuple))
for name, function in [("List", list), ("Tuple", tuple)]:
    start = time.perf_counter()
    data = function(range(1000000))
    print(name, "creation:", time.perf_counter()-start)
    start = time.perf_counter()
    print("Indexed value:", data[500000])
    print("Index time:", time.perf_counter()-start)