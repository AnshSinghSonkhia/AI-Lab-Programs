# Lists
list_example = [1, 2, 3, 4, 5]
print("List:", list_example)
print("Type of list:", type(list_example))
print("First element of the list:", list_example[0])
print("Last element of the list:", list_example[-1])
print("Length of the list:", len(list_example))
print()

# Tuples
tuple_example = (1, 2, 3, 4, 5)
print("Tuple:", tuple_example)
print("Type of tuple:", type(tuple_example))
print("First element of the tuple:", tuple_example[0])
print("Last element of the tuple:", tuple_example[-1])
print("Length of the tuple:", len(tuple_example))
print()

# Strings
string_example = "Hello, World!"
print("String:", string_example)
print("Type of string:", type(string_example))
print("First character of the string:", string_example[0])
print("Last character of the string:", string_example[-1])
print("Length of the string:", len(string_example))
print("Substring from index 7 to the end:", string_example[7:])
print()

# Ranges
range_example = range(1, 6)
print("Range:", list(range_example))  # Convert range to list for printing
print("Type of range:", type(range_example))
print("First element of the range:", range_example[0])
print("Last element of the range:", list(range_example)[-1])  # Convert range to list for accessing last element
print("Length of the range:", len(range_example))
print()

# Bytes
bytes_example = b'Hello'
print("Bytes:", bytes_example)
print("Type of bytes:", type(bytes_example))
print("First element of the bytes:", bytes_example[0])
print("Last element of the bytes:", bytes_example[-1])
print("Length of the bytes:", len(bytes_example))
print()

# Bytearrays
bytearray_example = bytearray(b'Hello')
print("Bytearray:", bytearray_example)
print("Type of bytearray:", type(bytearray_example))
print("First element of the bytearray:", bytearray_example[0])
print("Last element of the bytearray:", bytearray_example[-1])
print("Length of the bytearray:", len(bytearray_example))
