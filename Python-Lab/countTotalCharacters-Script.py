# Initialize an empty string to store the input text
text = ""

# Prompt the user to enter the text line by line until an empty line is entered
print("Enter the text (press Enter twice to finish):")
while True:
    line = input()
    if line:
        text += line + "\n"
    else:
        break

# Calculate the total number of characters
total_characters = len(text)

# Print the total number of characters
print("Total number of characters (including spaces and special characters):", total_characters)
