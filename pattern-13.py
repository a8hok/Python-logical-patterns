"""
OutPut Pattern:
A
BB
CCC
DDDD
EEEEE
"""

for x in range(65, 70):
    for y in range(65, x + 1):
        print(chr(x), end="")
    print()
