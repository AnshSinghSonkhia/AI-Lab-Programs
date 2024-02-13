rows = int(input("Enter the number of rows: "))

print(".")

for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(" ", end=" ")
    for j in range(0, 2 * i + 1):
        print("s", end=" ")
    print()


# OUTPUT

# Enter the number of rows: 5
# .
#         s 
#       s s s 
#     s s s s s 
#   s s s s s s s 
# s s s s s s s s s 