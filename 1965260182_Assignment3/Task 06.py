import time
from collections import defaultdict

# Railway timetable
timetable = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Vijayawada", "12:00", "12:05"),
            ("Hyderabad", "18:00", "18:10")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },

    "12602": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Katpadi", "09:00", "09:05"),
            ("Coimbatore", "14:00", "14:10")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },

    "12603": {
        "name": "Bengaluru Mail",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Katpadi", "10:00", "10:05"),
            ("Bengaluru", "13:00", "13:10")
        ],
        "days": {"Mon", "Tue", "Wed"}
    },

    "12604": {
        "name": "Madurai Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Villupuram", "11:00", "11:05"),
            ("Madurai", "16:00", "16:10")
        ],
        "days": {"Fri", "Sat", "Sun"}
    },

    "12605": {
        "name": "Mysuru Express",
        "stops": [
            ("Chennai", "10:00", "10:10"),
            ("Katpadi", "12:00", "12:05"),
            ("Mysuru", "17:00", "17:10")
        ],
        "days": {"Sun", "Tue", "Thu"}
    }
}

# Find trains without an index
def search_trains(station, day):

    result = []

    for number, info in timetable.items():

        if day in info["days"]:

            for stop, arrival, departure in info["stops"]:

                if stop == station:
                    result.append(
                        (number, info["name"], arrival, departure)
                    )

    return sorted(result, key=lambda x: x[3])

# Create station index
def create_index():

    index = defaultdict(list)

    for number, info in timetable.items():

        for station, arrival, departure in info["stops"]:

            index[station].append(
                (number, arrival, departure, info["days"])
            )

    return index

index = create_index()

# Search using index
def indexed_search(station, day):

    result = []

    for number, arrival, departure, days in index.get(station, []):

        if day in days:

            result.append(
                (number, timetable[number]["name"],
                 arrival, departure)
            )

    return sorted(result, key=lambda x: x[3])

print("Trains at Chennai on Monday:")

for train in indexed_search("Chennai", "Mon"):
    print(train)

# Display complete timetable
print("\nComplete Railway Timetable:")

for number, info in timetable.items():

    print("\nTrain:", number)
    print("Name:", info["name"])
    print("Running days:", info["days"])

    for station, arrival, departure in info["stops"]:
        print(station, arrival, departure)

# Test unknown station
print("\nUnknown station:",
      indexed_search("Unknown", "Mon"))

# Test train not running on the selected day
print("Coimbatore on Monday:",
      indexed_search("Coimbatore", "Mon"))

# Performance testing
def generate_trains(n):

    stations = [
        "Chennai", "Katpadi", "Salem",
        "Madurai", "Bengaluru"
    ]

    data = {}

    for i in range(n):

        stops = [
            (stations[(i+j) % len(stations)],
             "10:00", "10:10")
            for j in range(5)
        ]

        data[str(i)] = {
            "name": f"Train {i}",
            "stops": stops,
            "days": {"Mon", "Wed", "Fri"}
        }

    return data

print("\nPerformance comparison:")

for n in [100, 1000, 10000]:

    data = generate_trains(n)

    start = time.perf_counter()

    for number, info in data.items():
        for stop, arrival, departure in info["stops"]:
            if stop == "Chennai":
                pass

    scan_time = time.perf_counter() - start

    start = time.perf_counter()

    temp_index = defaultdict(list)

    for number, info in data.items():
        for stop, arrival, departure in info["stops"]:
            temp_index[stop].append(number)

    index_time = time.perf_counter() - start

    print("Trains:", n)
    print("Without index:", scan_time)
    print("Index creation:", index_time)