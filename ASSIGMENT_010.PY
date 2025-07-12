# 1. for loop
for i in range(1, 6):
    print(i)  # Output: 1 to 5

# 2. while loop
i = 1
while i <= 5:
    print(i)
    i += 1  # Output: 1 to 5

# 3. Nested Loops
for i in range(1, 3):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
# Output:
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# i=2, j=3

# 4. break in loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# 5. continue in loop
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4
