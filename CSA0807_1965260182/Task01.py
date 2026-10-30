def separate_if(units, ration, senior):
    if units <= 100:
        print("Full Subsidy")
    if 101 <= units <= 200 and ration:
        print("Partial Subsidy")
    if units > 200 and senior:
        print("Senior Citizen Subsidy")
    if units > 200 and not senior:
        print("No Subsidy")
    if 101 <= units <= 200 and not ration:
        print("No Subsidy")
def using_elif(units, ration, senior):
    if units <= 100:
        return "Full Subsidy"
    elif 101 <= units <= 200:
        if ration:
            return "Partial Subsidy"
        else:
            return "No Subsidy"
    else:
        if senior:
            return "Senior Citizen Subsidy"
        else:
            return "No Subsidy"
households = [
    (100, False, False),
    (101, True, False),
    (101, False, False),
    (150, True, False),
    (200, True, False),
    (200, False, False),
    (201, False, False),
    (201, False, True)
]
for h in households:
    units, ration, senior = h
    print("\nHousehold:", h)
    print("Separate if:")
    separate_if(units, ration, senior)
    print("If-elif-else:", using_elif(units, ration, senior))