rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("s", end=" ")
    print()

# OUTPUT

# Enter the number of rows: 5

# s s s s s 
# s s s s 
# s s s 
# s s 
# s

# Replace s with *