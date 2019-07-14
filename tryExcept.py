# specify what made it break
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: #store error as a variable
   print(err) # prints actual error message
except ValueError:
    print("Invalid input")

# best practice, except for SPECIFIC ERRORS