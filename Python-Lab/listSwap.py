# To Swap 1st and last elements of a list.
my_list = [1, 2, 3, 4, 5]

# Before swapping
print("Before swapping:", my_list)

# Swapping first and last elements
if len(my_list) >= 2:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]

# After swapping
print("After swapping:", my_list)

# OUTPUT

# Before swapping: [1, 2, 3, 4, 5]
# After swapping: [5, 2, 3, 4, 1]
