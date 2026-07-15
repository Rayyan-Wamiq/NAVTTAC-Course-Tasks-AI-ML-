try:
    number = int(input("Enter a number:"))
    number2 = int(input("Enter another number:"))
    print(number/number2)
except ValueError:
    print("That wasn't a valid number")
except ZeroDivisionError:
    print("Cannot divided by zero")

else:
    print("The division result is successful")
finally:
    print("Calculation attempt completes")