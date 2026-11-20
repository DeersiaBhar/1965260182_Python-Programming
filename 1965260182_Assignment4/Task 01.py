
import random
import time
def weekly_totals(readings):
    return [sum(readings[i:i+7])
            for i in range(0, len(readings), 7)]
def moving_naive(readings):
    if len(readings) < 7:
        return []
    return [
        sum(readings[i:i+7]) / 7
        for i in range(len(readings)-6)
    ]
def moving_running(readings):
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
    readings = [random.randint(0, 80) for _ in range(365)]
    weeks = weekly_totals(readings)
    print("Weekly totals:", weeks)
    print("Wettest week:", weeks.index(max(weeks))+1)
    print("Driest week:", weeks.index(min(weeks))+1)
    print("Moving averages:",
          moving_running(readings)[:10])
    dry_days = [
        i+1 for i, value in enumerate(readings)
        if value == 0
    ]
    print("Dry days:", dry_days)
    print("Slice readings[7:14]:", readings[7:14])
    print("Last 7 readings:", readings[-7:])
    print("Every 7th reading:", readings[::7])
    print("Empty list:", moving_running([]))
    print("Short list:", moving_running([2, 3, 4]))
    print("\nPerformance comparison")
    for n in [365, 36500, 365000]:
        data = [random.randint(0, 80) for _ in range(n)]
        start = time.perf_counter()
        moving_naive(data)
        t1 = time.perf_counter() - start
        start = time.perf_counter()
        moving_running(data)
        t2 = time.perf_counter() - start
        print(n, "Naive:", t1, "Running:", t2)
if __name__ == "__main__":
    main()