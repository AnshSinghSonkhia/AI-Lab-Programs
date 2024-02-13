# Reverse the list

# Example list
my_list = [1, 2, 3, 4, 5]

# Before reversing
print("Before reversing:", my_list)

# Reversing the list using slicing
reversed_list = my_list[::-1]

# After reversing
print("After reversing:", reversed_list)

# Example list 2 - using reverse() function
my_list2 = [1, 2, 3, 4, 5]

# Before reversing
print("Before reversing:", my_list2)

# Reversing the list in-place
my_list2.reverse()

# After reversing
print("After reversing:", my_list2)

# OUTPUT

# Before reversing: [1, 2, 3, 4, 5]
# After reversing: [5, 4, 3, 2, 1]
# Before reversing: [1, 2, 3, 4, 5]
# After reversing: [5, 4, 3, 2, 1]