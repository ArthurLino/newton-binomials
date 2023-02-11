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

multiplyer = 1

print(f"(a+b)^{a_index} =")
result=0

for loop_index, b_index in enumerate(range(a_index, -1, -1), start=1):
    print(f"{loop_index}° nomial: +{multiplyer} * {a}^{b_index} * {b}^{a_index - b_index}")
    result += multiplyer * a**b_index * b **(a_index - b_index)
    multiplyer *= b_index / loop_index
    multiplyer = math.ceil(multiplyer)

print(f"Result: {result}")
