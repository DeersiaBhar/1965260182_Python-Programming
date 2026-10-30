import time
items = [f"Item{i}:Rs{i % 50}" for i in range(200000)]
def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text
def build_join(parts):
    return ";".join(parts) + ";"
def build_fstring(parts):
    return "".join(f"{p};" for p in parts)
start = time.perf_counter()
a = build_plus(items)
t1 = time.perf_counter() - start
start = time.perf_counter()
b = build_join(items)
t2 = time.perf_counter() - start
start = time.perf_counter()
c = build_fstring(items)
t3 = time.perf_counter() - start
print("Plus and Join same:", a == b)
print("Plus and f-string same:", a == c)
print("Length:", len(b))
print("Plus time:", t1)
print("Join time:", t2)
print("F-string time:", t3)