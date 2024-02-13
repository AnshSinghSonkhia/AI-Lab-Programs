def check_type(var):
    if isinstance(var, bool):
        print("Boolean")
    elif isinstance(var, int):
        print("Integer")
    elif isinstance(var, float):
        print("Float")
    elif isinstance(var, str):
        print("String")
    else:
        print("Unknown type")

# Input number from the user
num = 4.55
check_type(num)

# Example with other types
check_type(5)
check_type("Hello")
check_type(True)


