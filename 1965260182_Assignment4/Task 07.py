import re
import time
def normalize_phone(phone):
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits
def normalize_name(name):
    return " ".join(
        re.findall(r"[a-z]+", (name or "").lower())
    )
def merge_contacts(contacts):
    merged = {}
    for contact in contacts:
        name = contact.get("name", "")
        email = contact.get("email", "").lower()
        phones = contact.get("phones", [])
        normalized = {
            normalize_phone(p) for p in phones
        }
        normalized.discard("")
        if not normalized:
            normalized = {
                "NO_PHONE_" + str(len(merged))
            }
        for phone in normalized:
            if phone not in merged:
                merged[phone] = {
                    "names": set(),
                    "phones": set(),
                    "emails": set()
                }
            if name:
                merged[phone]["names"].add(name)
            if email:
                merged[phone]["emails"].add(email)
            for p in phones:
                if p:
                    merged[phone]["phones"].add(p)
    return merged
contacts = [
    {
        "name": "Dr. Ravi",
        "phones": ["+91 98400 12345"],
        "email": "ravi@gmail.com"
    },
    {
        "name": "Ravi Kumar",
        "phones": ["9840012345"],
        "email": "ravi.work@gmail.com"
    },
    {
        "name": "Meena",
        "phones": ["9000011111"],
        "email": "meena@gmail.com"
    },
    {
        "name": "Meena",
        "phones": [],
        "email": "meena2@gmail.com"
    }
]
result = merge_contacts(contacts)
print("Merged Contacts")
for phone, details in result.items():
    print("\nPhone:", phone)
    print("Names:", details["names"])
    print("Numbers:", details["phones"])
    print("Emails:", details["emails"])
for n in [1000, 100000]:
    data = [
        {
            "name": "Person " + str(i),
            "phones": [str(9000000000 + i)],
            "email": "person" + str(i) + "@gmail.com"
        }
        for i in range(n)
    ]
    start = time.perf_counter()
    merged = merge_contacts(data)
    elapsed = time.perf_counter() - start
    print("\nContacts:", n)
    print("Time:", elapsed)
    print("Merged records:", len(merged))
n = 100000
print("Pairwise comparisons:",
      n * (n - 1) // 2)