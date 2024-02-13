# Program to sum 2 numbers
a = 20
b = 30
c = a + b
print(c)

# Using Conditionals

if c > 30:
    print("Hi 30+")
else:
    print ("Bye 30-")
    
if (c < 30):
    print("New Hi")
else:
    print ("Bye New")


if (0):
    print("1 ki baat")
else:
    print("0 ki baat")

# WAP to determine odd or even number

num = int(input("Enter any Number:   "))

# Check if the number is divisible by 2
if (num % 2):
    print("Odd")    # If the remainder after dividing by 2 is non-zero, then the number is odd
else:
    print("Even")   # If the remainder after dividing by 2 is zero, then the number is even
    
# In Python, the integer 0 evaluates to False in a conditional statement. 
# Therefore, when the reminder is 0, else statement runs - even
# when the reminder is 1, if statement runs



