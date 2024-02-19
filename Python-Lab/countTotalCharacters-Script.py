# Initialize an empty string to store the input text
text = """    """

# Use of triple quotation marks to take multiline text.

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

# Calculate the total number of words
words = text.split()
total_words = len(words)

# Print the total number of words
print("Total number of words:  ", total_words)
