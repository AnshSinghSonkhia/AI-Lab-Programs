rows = int(input("Enter the number of rows: "))
print(".")

# Upper half of the pyramid
for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(" ", end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

# Lower half of the pyramid
for i in range(rows - 2, -1, -1):
    for j in range(0, rows - i - 1):
        print(" ", end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()


# OUTPUT

# Enter the number of rows: 5
# .
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 