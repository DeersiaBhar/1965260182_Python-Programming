import time
trains = {
    "12601": {
        "name": "Chennai Mail",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Arakkonam", "07:20", "07:22"),
            ("Katpadi", "08:30", "08:35")
        ],
        "days": {"Mon", "Tue", "Wed"}
    },
    "12602": {
        "name": "West Coast Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Katpadi", "09:10", "09:15"),
            ("Bengaluru", "12:00", "12:10")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },
    "12603": {
        "name": "Kaveri Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Villupuram", "10:00", "10:05"),
            ("Trichy", "13:00", "13:05")
        ],
        "days": {"Tue", "Thu"}
    },
    "12604": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Katpadi", "11:00", "11:05"),
            ("Coimbatore", "16:00", "16:10")
        ],
        "days": {"Daily"}
    },
    "12605": {
        "name": "Pandian Express",
        "stops": [
            ("Chennai", "20:00", "20:15"),
            ("Villupuram", "22:00", "22:05"),
            ("Madurai", "04:00", "04:10")
        ],
        "days": {"Daily"}
    }
}
for number, train in trains.items():
    print("\nTrain:", number, train["name"])
    for station, arrival, departure in train["stops"]:
        print(station, arrival, departure)
def find_trains(station, day):
    result = []
    for number, train in trains.items():
        if day not in train["days"] and "Daily" not in train["days"]:
            continue
        for stop, arrival, departure in train["stops"]:
            if stop == station:
                result.append(
                    (number, train["name"], departure)
                )
    return sorted(result, key=lambda x: x[2])
print("\nChennai on Monday:")
print(find_trains("Chennai", "Mon"))
station_index = {}
for number, train in trains.items():
    for station, arrival, departure in train["stops"]:
        station_index.setdefault(station, []).append(
            (number, train["name"], departure, train["days"])
        )
def indexed_search(station, day):
    result = []
    for number, name, departure, days in station_index.get(station, []):
        if day in days or "Daily" in days:
            result.append((number, name, departure))
    return sorted(result, key=lambda x: x[2])
print("\nIndexed search:")
print(indexed_search("Katpadi", "Mon"))
print("\nUnknown station:")
print(find_trains("Unknown", "Mon"))