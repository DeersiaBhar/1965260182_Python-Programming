import re
import time

# Normalize phone numbers
def normalize_number(number):

    if not number:
        return ""

    digits = re.sub(r"\D", "", number)

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits

# Normalize names
def normalize_name(name):

    return " ".join(
        re.findall(r"[a-z]+", (name or "").lower())
    )

# Merge contacts
def merge_contacts(contact_lists):

    merged = {}

    for contacts in contact_lists:

        for contact in contacts:

            name = contact.get("name", "")
            email = contact.get("email", "").lower()

            phones = contact.get("phones", [])

            if isinstance(phones, str):
                phones = [phones]
            numbers = {
                normalize_number(p)
                for p in phones
            }
            numbers.discard("")
            if not numbers:
                merged[f"unknown{len(merged)}"] = {
                    "names": {name} if name else set(),
                    "numbers": set(),
                    "emails": {email} if email else set()
                }
                continue
            existing = [
                merged[number]
                for number in numbers
                if number in merged
            ]
            if existing:
                person = existing[0]
                for other in existing[1:]:
                    person["names"].update(other["names"])
                    person["numbers"].update(other["numbers"])
                    person["emails"].update(other["emails"])
            else:
                person = {
                    "names": set(),
                    "numbers": set(),
                    "emails": set()
                }
            if name:
                person["names"].add(name)
            person["numbers"].update(numbers)
            if email:
                person["emails"].add(email)
            for number in person["numbers"]:
                merged[number] = person
    result = []
    seen = set()
    for person in merged.values():
        if id(person) not in seen:
            seen.add(id(person))
            result.append({
                "names": sorted(person["names"]),
                "numbers": sorted(person["numbers"]),
                "emails": sorted(person["emails"])
            })
    return result
phone1 = [
    {
        "name": "Dr. Ravi",
        "phones": ["+91 98400 12345"],
        "email": "ravi@example.com"
    },
    {
        "name": "Anita",
        "phones": ["9000011111"],
        "email": "anita@example.com"
    }
]
phone2 = [
    {
        "name": "ravi kumar",
        "phones": ["9840012345", "044-22223333"],
        "email": "RAVI@example.com"
    },
    {
        "name": "Kiran",
        "phones": [],
        "email": "kiran@example.com"
    }
]
sim = [
    {
        "name": "Ravi",
        "phones": ["+91-98400-12345"],
        "email": ""
    },
    {
        "name": "Anita S",
        "phones": ["9000011111"],
        "email": ""
    }
]
result = merge_contacts([phone1, phone2, sim])
print("Merged Contacts:")
for contact in result:
    print(contact)
def performance_test(n):
    contacts = []
    for i in range(n):
        contacts.append([{
            "name": f"Person {i}",
            "phones": [f"900{i:07d}"],
            "email": f"user{i}@gmail.com"
        }])
    start = time.perf_counter()
    merged_result = merge_contacts(contacts)
    end = time.perf_counter()
    print("\nNumber of contacts:", n)
    print("Execution time:", end-start)
    print("Merged contacts:", len(merged_result))
performance_test(1000)
performance_test(100000)