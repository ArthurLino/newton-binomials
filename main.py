import math

super_s = [n for n in "⁰¹²³⁴⁵⁶⁷⁸⁹"]

print("For (a+b)^x: ")

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    a_index = int(input("Enter x: "))
except:
    a, b, a_index = "a", "b", 5
    print("Not all input values are usable. ")

multiplyer = 1

print("Expresison: ")

for loop_index, b_index in enumerate(range(a_index, -1, -1), start=1):
    if loop_index != 1:
        print("+", end=" ")
    if multiplyer != 1:
        print('{}'.format(multiplyer), end='*')
    if b_index > 0:
        print('{}{}'.format(a ,''.join(super_s[int(l)] for l in str(b_index))), end='')
    if a_index-b_index > 0 :
        print('*{}{}'.format(b, ''.join(super_s[int(l)] for l in str(a_index-b_index))), end=' ')
    multiplyer *= b_index / loop_index
    multiplyer = math.ceil(multiplyer)
