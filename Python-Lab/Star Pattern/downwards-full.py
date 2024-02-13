rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(" ", end=" ")
    for j in range(0, 2 * i - 1):
        print("s", end=" ")
    print()

#OUTPUT

# Enter the number of rows: 5
# s s s s s s s s s 
#   s s s s s s s 
#     s s s s s 
#       s s s 
#         s 