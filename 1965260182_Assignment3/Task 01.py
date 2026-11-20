import random
import time
def weekly_totals(readings):
    return [
        sum(readings[i:i+7])
        for i in range(0, len(readings)-6, 7)
    ]
def naive_average(readings):
    return [
        sum(readings[i:i+7]) / 7
        for i in range(len(readings)-6)
    ]
def running_average(readings):
    if len(readings) < 7:
        return []
    total = sum(readings[:7])
    result = [total / 7]
    for i in range(7, len(readings)):
        total += readings[i] - readings[i-7]
        result.append(total / 7)
    return result
def main():
    random.seed(10)
    readings = [round(random.uniform(0, 30), 1)
                for _ in range(365)]
    readings[10] = 0
    readings[100] = 0
    weeks = weekly_totals(readings)
    print("Weekly totals:", weeks)
    print("Maximum rainfall:", max(readings))
    print("Maximum position:", readings.index(max(readings)) + 1)
    print("Minimum rainfall:", min(readings))
    print("Minimum position:", readings.index(min(readings)) + 1)
    print("Wettest week:", weeks.index(max(weeks)) + 1)
    print("Driest week:", weeks.index(min(weeks)) + 1)
    print("Moving average:", naive_average(readings))
    print("Dry days:", [i+1 for i, x in enumerate(readings) if x == 0])
    print("\nSlicing:")
    print("readings[7:14]:", readings[7:14])
    print("readings[-7:]:", readings[-7:])
    print("readings[::7]:", readings[::7])
    print("\nTiming comparison:")
    for n in [365, 36500, 365000]:
        data = [random.randint(0, 30) for _ in range(n)]
        start = time.perf_counter()
        a = naive_average(data)
        t1 = time.perf_counter() - start
        start = time.perf_counter()
        b = running_average(data)
        t2 = time.perf_counter() - start
        print(f"{n} readings")
        print("Naive time:", t1)
        print("Running sum time:", t2)
        print("Results same:", a == b)
    print("Empty list:", running_average([]))
    print("Short list:", running_average([1, 2, 3]))
if __name__ == "__main__":
    main()