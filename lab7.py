# Task 1: File I/O with Names
# Write a list of names to a file called names.txt
names = ['Elchibek', 'Emil', 'Muha']

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read and print the contents of the file
print("Task 1: File Contents")
with open("names.txt", "r") as file:
    print(file.read())


# Task 2: List Operations
# Create the initial list
numbers = [10, 20, 30, 40, 50]
print(f"Initial list: {numbers}")

# Add 60 to the list
numbers.append(60)
print(f"After adding 60: {numbers}")

# Insert 5 at the beginning
numbers.insert(0, 5)
print(f"After inserting 5: {numbers}")

# Remove 40
numbers.remove(40)
print(f"After removing 40: {numbers}")

# Sort the list
numbers.sort()
print(f"After sorting: {numbers}")

# Reverse the list
numbers.reverse()
print(f"After reversing: {numbers}")


# Task 3: String Manipulation
text = "Learning Python is exciting!"

# Convert the string to uppercase and lowercase
print(f"\nUppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# Count how many times the letter "i" appears
count_i = text.count("i")
print(f"The letter 'i' appears {count_i} times.")

# Replace the word "exciting" with "fun"
new_text = text.replace("exciting", "fun")
print(f"New string: {new_text}")

# Split the string into a list of words and print each individually
print("Individual words:")
words = text.split()
for word in words:
    print(word)