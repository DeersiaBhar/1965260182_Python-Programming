import sqlite3
import time
import random
import cProfile
import pandas as pd
from collections import defaultdict
def generate_data(stations):
    rows = []
    for i in range(stations):
        for day in range(365):
            pm25 = round(random.uniform(10, 150), 2)
            rows.append((f"Station_{i}", day, pm25))
    return rows
def python_loops(rows):
    total = defaultdict(float)
    count = defaultdict(int)
    for station, day, pm25 in rows:
        key = (station, day)
        total[key] += pm25
        count[key] += 1
    return {
        key: total[key] / count[key]
        for key in total
    }
def pandas_method(rows):
    df = pd.DataFrame(
        rows,
        columns=["station", "day", "pm25"]
    )
    return df.groupby(
        ["station", "day"]
    )["pm25"].mean()
def sql_method(rows):
    con = sqlite3.connect(":memory:")
    con.execute("""
    CREATE TABLE readings (
        station TEXT,
        day INTEGER,
        pm25 REAL
    )
    """)
    con.executemany(
        "INSERT INTO readings VALUES (?, ?, ?)",
        rows
    )
    result = con.execute("""
    SELECT station, day, AVG(pm25)
    FROM readings
    GROUP BY station, day
    """).fetchall()
    con.close()
    return result
for stations in [1, 12, 120]:
    rows = generate_data(stations)
    print("\nStations:", stations)
    print("Total rows:", len(rows))
    start = time.perf_counter()
    result1 = python_loops(rows)
    print("Python time:", time.perf_counter() - start)
    start = time.perf_counter()
    result2 = pandas_method(rows)
    print("Pandas time:", time.perf_counter() - start)
    start = time.perf_counter()
    result3 = sql_method(rows)
    print("SQL time:", time.perf_counter() - start)
    print("Python and Pandas results agree:",
          all(abs(result1[k] - result2[k]) < 0.000001
              for k in result1))
print("\nProfiling Python loops:")
cProfile.run("python_loops(generate_data(12))")