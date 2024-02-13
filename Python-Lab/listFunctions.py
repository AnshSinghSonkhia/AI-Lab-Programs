# Create a list
my_list = [1, 2, 3, 4, 5]

# Append: Add an element to the end of the list
my_list.append(6)
print("List after appending 6:", my_list)

# Extend: Extend the list by appending elements from another iterable
my_list.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", my_list)

# Insert: Insert an element at a specified position
my_list.insert(0, 0)
print("List after inserting 0 at the beginning:", my_list)

# Remove: Remove the first occurrence of a value
my_list.remove(3)
print("List after removing 3:", my_list)

# Pop: Remove and return the element at a specified position (default is the last element)
popped_element = my_list.pop(2)
print("Popped element at index 2:", popped_element)
print("List after popping element at index 2:", my_list)

# Index: Return the index of the first occurrence of a value
index_of_5 = my_list.index(5)
print("Index of 5 in the list:", index_of_5)

# Count: Return the number of occurrences of a value
count_of_2 = my_list.count(2)
print("Count of 2 in the list:", count_of_2)

# Sort: Sort the list in ascending order
my_list.sort()
print("Sorted list:", my_list)

# Reverse: Reverse the elements of the list
my_list.reverse()
print("Reversed list:", my_list)

# Clear: Remove all elements from the list
my_list.clear()
print("List after clearing:", my_list)


# Output

# List after appending 6: [1, 2, 3, 4, 5, 6]
# List after extending with [7, 8, 9]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# List after inserting 0 at the beginning: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# List after inserting 66 at the 3rd position: [0, 1, 2, 66, 3, 4, 5, 6, 7, 8, 9]
# List after removing 3: [0, 1, 2, 66, 4, 5, 6, 7, 8, 9]
# Popped element at index 2: 2
# List after popping element at index 2: [0, 1, 66, 4, 5, 6, 7, 8, 9]
# Index of 5 in the list: 4
# Count of 2 in the list: 0
# Sorted list: [0, 1, 4, 5, 6, 7, 8, 9, 66]
# Reversed list: [66, 9, 8, 7, 6, 5, 4, 1, 0]
# List after clearing: []