import re
import sqlite3
import time
from collections import Counter
POSITIVE = {
    "good", "clean", "fast", "helpful", "improved"
}
NEGATIVE = {
    "bad", "dirty", "slow", "rude", "smoke", "broken"
}
NEGATORS = {"not", "never", "no"}
def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0
    for i, word in enumerate(words):
        if word in POSITIVE:
            value = 1
        elif word in NEGATIVE:
            value = -1
        else:
            value = 0
        if i > 0 and words[i - 1] in NEGATORS:
            value *= -1
        total += value
    return total
def label(text):
    s = score(text)
    if s > 0:
        return "positive"

    elif s < 0:
        return "negative"
    else:
        return "neutral"
def summarise(text, k=2):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    words = re.findall(r"\w+", text.lower())
    frequency = Counter(words)
    ranked = []
    for sentence in sentences:
        sentence_words = re.findall(
            r"\w+", sentence.lower()
        )
        value = sum(
            frequency[word]
            for word in sentence_words
            if len(word) > 3
        )
        ranked.append((value, sentence))
    ranked.sort(reverse=True)
    return " ".join(
        sentence for value, sentence in ranked[:k]
    )
complaints = [
    "Roads are clean and the bus was fast.",
    "Smoke from the factory, air is bad.",
    "The staff were not helpful.",
    "Not bad, service improved.",
    "The road is dirty and the bus is slow."
] * 10
print("SENTIMENT ANALYSIS")
for complaint in complaints[:5]:
    print(label(complaint), "|", complaint)
print("\nTEXT SUMMARY")
text = "The roads are clean. The air is bad. Smoke is coming from factories. The buses are fast."
print(summarise(text))
print("\nDATABASE INDEX TEST")
con = sqlite3.connect(":memory:")
con.execute("""
CREATE TABLE readings (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")
data = [
    (f"Station_{i % 100}", f"2026-10-{i % 28 + 1:02d}", float(i % 150))
    for i in range(100000)
]
con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)",
    data
)
con.commit()
query = """
SELECT AVG(pm25)
FROM readings
WHERE station = ? AND day = ?
"""
start = time.perf_counter()
for i in range(100):
    con.execute(
        query, ("Station_42", "2026-10-15")
    ).fetchone()
before = time.perf_counter() - start
con.execute("""
CREATE INDEX idx_station_day
ON readings(station, day)
""")
start = time.perf_counter()
for i in range(100):
    con.execute(
        query, ("Station_42", "2026-10-15")
    ).fetchone()
after = time.perf_counter() - start
print("Before index:", before)
print("After index:", after)
con.close()