"""
OutPut Pattern:
1
22
333
4444
55555
"""

for x in range(1, 6):
    for y in range(1, x + 1):
        print(x, end="")
    print()
