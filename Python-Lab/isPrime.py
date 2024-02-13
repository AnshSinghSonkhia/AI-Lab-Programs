def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # Check divisibility starting from 3 up to the square root of num
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

# Input number from the user
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


# OUTPUT

# Enter a number: 83
# 83 is a prime number.

# Enter a number: 46
# 46 is not a prime number.