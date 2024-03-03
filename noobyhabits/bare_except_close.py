# Using a bare except clause
def bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except:  # This catches all exceptions, including KeyboardInterrupt
            print("Not a number, try again")


# Correctly catching a specific exception
def correct_bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except ValueError:  # Correctly catching the specific exception
            print("Not a number, try again")
        except KeyboardInterrupt:  # Optionally, handle keyboard interrupts gracefully
            print("\nProgram interrupted by the user. Exiting...")
            break

bare_except()