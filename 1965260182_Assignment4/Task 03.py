import random
import time
from collections import Counter
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]
STOP = {"not", "high"}
def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.lower().split():
            word = word.strip(".,!?")
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )[:k]
print(top(frequencies(calls, STOP), 3))
complaints = [
    ("Chennai", "Seeds delayed"),
    ("Salem", "Fertiliser shortage"),
    ("Chennai", "Water shortage"),
    ("Madurai", "Crop damage")
]
districts = {}
for district, complaint in complaints:
    districts.setdefault(district, []).append(complaint)
print("District complaints:", districts)
words = "apple mango apple orange mango apple".split()
print("Counter:", Counter(words))
for n in [1000, 10000, 100000]:
    data = [
        "seeds price crop soil water"
        for i in range(n)
    ]
    start = time.perf_counter()
    frequencies(data, set())
    dictionary_time = time.perf_counter()-start
    start = time.perf_counter()
    Counter(" ".join(data).split())
    counter_time = time.perf_counter()-start
    print(n, "Dictionary:", dictionary_time,
          "Counter:", counter_time)