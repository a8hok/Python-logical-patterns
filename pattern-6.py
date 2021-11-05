"""
OutPut Pattern:
55555
44444
33333
22222
11111
"""
for x in range(5, 0, -1):
    for y in range(5, 0, -1):
        print(x, end="")
    print()