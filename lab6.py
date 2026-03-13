def positive_Number():
    while True:
        try:
            # asking for input and converting to a float
            user_input = float(input("Enter a number (negative to stop): "))

            # check if the number is negative to exit
            if user_input < 0:
                print("Negative number detected. Exiting...")
                break

            # printing the non-negative number using f-string
            print(f"You entered: {user_input}")

        except ValueError:
            print("Please enter a valid numeric value.")


def skip_Divisible_3():
    while True:
        try:
            user_input = int(input("Enter an integer (0 to stop): "))

            # stop the loop if the user enters 0
            if user_input == 0:
                print("0 entered. Program stopped.")
                break

            # skip numbers divisible by 3
            if user_input % 3 == 0:
                continue

            # print all other numbers using f-string
            print(f"Number: {user_input}")

        except ValueError:
            print("Please enter a valid integer.")

