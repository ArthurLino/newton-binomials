""" (a+b)^x """
import math

print("For (a+b)^x: ")
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    a_index = int(input("Enter x: "))
except:
    a, b, a_index = 1, 1, 1
    print("Not all input values are usable. Values were set to 1 automatically. ")

multiplier = 1

print(f"Then (a+b)^{a_index} =")
result = (a+b)**a_index

for loop_index, b_index in enumerate(range(a_index, -1, -1), start=1):
    print(f"{loop_index}° nomial: +{multiplier} * {a}^{b_index} * {b}^{a_index - b_index}")
    multiplier *= b_index / loop_index
    multiplier = math.ceil(multiplier)

print(f"Result: {result}")
