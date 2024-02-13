#  Python program that checks whether a given number exists in a list:

my_list = [1, 3, 5, 7, 9]

# Number to check
number_to_check = int(input("Enter a number to check: "))

# Check if the number exists in the list
if number_to_check in my_list:
    print("Number", number_to_check, "exists in the list.")
else:
    print("Number", number_to_check, "does not exist in the list.")

# OUTPUT

# Enter a number to check: 5
# Number 5 exists in the list.

# Enter a number to check: 46
# Number 46 does not exist in the list.