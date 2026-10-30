def normalise(text):
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()
def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]
    return (
        state.isalpha()
        and district.isdigit()
        and series.isalpha()
        and len(series) in (1, 2)
        and number.isdigit()
    )
def format_number(reg):
    if is_valid(reg):
        return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]
    return "Invalid Number"
vehicles = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "MH 12 CD 9876",
    "DL 03 C 4321"
]
for raw in vehicles:
    reg = normalise(raw)
    if is_valid(reg):
        print(raw, "->", reg, "VALID")
        print("Receipt:", format_number(reg))
    else:
        print(raw, "->", reg, "INVALID")