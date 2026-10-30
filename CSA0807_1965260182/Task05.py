def add_item_buggy(item, order=[]):
    order.append(item)
    return order
def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order
print("Buggy Function:")
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))
print("\nCorrect Function:")
print(add_item("Tea"))
print(add_item("Vada"))
def student(name, age=18):
    print(name, age)
student("Arun")
student("Ravi", 19)
def calculate_bill(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst
total, gst = calculate_bill(1000)
print("\nTotal:", total)
print("GST:", gst)
count = 0
def global_example():
    global count
    count += 1
    print("Global count:", count)
global_example()
def local_example():
    message = "Local variable"
    print(message)
local_example()
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("Nonlocal:", x)
    inner()
outer()
print("\nDefault values:", add_item_buggy.__defaults__)