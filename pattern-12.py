"""
OutPut Pattern:
1
12
123
1234
12345
"""

for x in range(1, 6):
    for y in range(1, x + 1):
        print(y, end="")
    print()