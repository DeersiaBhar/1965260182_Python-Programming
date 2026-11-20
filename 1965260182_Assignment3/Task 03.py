import random
import re
import time
from collections import Counter
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]
STOP = {"not", "high"}
# TODO 1
def frequencies(texts, stop):
    counts = {}
    for text in texts:
        words = re.findall(r"\b[a-z]+\b", text.lower())
        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts
# TODO 2
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )[:k]
print(top(frequencies(calls, STOP), 3))
def group_complaints(records):
    district_data = {}
    for district, complaint in records:
        district_data.setdefault(district, []).append(complaint)
    return district_data
records = [
    ("Chennai", "Seeds delayed"),
    ("Avadi", "Fertiliser price high"),
    ("Chennai", "Water shortage"),
    ("Avadi", "Subsidy not received")
]
print("District complaints:")
print(group_complaints(records))
def list_count_method(texts):
    words = []
    for text in texts:
        words.extend(text.lower().split())
    return {word: words.count(word) for word in set(words)}
print("\nPerformance testing:")
vocabulary = ["seeds", "crop", "water", "price", "soil"]
for n in [1000, 10000, 100000]:
    data = [
        " ".join(random.choices(vocabulary, k=8))
        for _ in range(n)
    ]
    start = time.perf_counter()
    result1 = frequencies(data, set())
    t1 = time.perf_counter() - start
    start = time.perf_counter()
    result2 = list_count_method(data)
    t2 = time.perf_counter() - start
    start = time.perf_counter()
    result3 = Counter(" ".join(data).split())
    t3 = time.perf_counter() - start
    print("Complaints:", n)
    print("Dictionary:", t1)
    print("List count:", t2)
    print("Counter:", t3)