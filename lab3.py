# 1. Flowchart into code
# get input from the user
user_input = input("Enter a value: ")

# checking if the intput is bad (empty)
# the loop continues while the condition is True
while user_input == "":
    # display error
    print("Error: Input cannot be empty.")

    # get input again
    user_input = input("Please enter a valid value: ")

print("Thank you for the valid input!")

# 2. Even numbers from 1 to 20
# iterating through 1 to 2o numbers
for number in range (1, 20):
    # finding even numbers
    if number % 2 == 0:
        # displaying even numbers
        print(number)