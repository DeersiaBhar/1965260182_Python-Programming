import time
ai_elective = {
    "192311001", "192311004",
    "192311007", "192311009"
}
iot_elective = {
    "192311002", "192311004",
    "192311009", "192311010"
}
all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}
both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (
    ai_elective | iot_elective
)
print("clash      :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither    :", sorted(neither))
both2 = ai_elective.intersection(iot_elective)
one2 = ai_elective.symmetric_difference(iot_elective)
neither2 = all_students.difference(
    ai_elective.union(iot_elective)
)
print("Methods verified:",
      both == both2 and
      exactly_one == one2 and
      neither == neither2)
print("Empty:", set() & iot_elective)
print("Identical:", ai_elective ^ ai_elective)
for n in [10000, 100000, 1000000]:
    values = list(range(n))
    values_set = set(values)
    start = time.perf_counter()
    print(n-1 in values)
    list_time = time.perf_counter()-start
    start = time.perf_counter()
    print(n-1 in values_set)
    set_time = time.perf_counter()-start
    print("List time:", list_time)
    print("Set time:", set_time)