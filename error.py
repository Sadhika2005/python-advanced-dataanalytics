try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b

except ValueError:
    print("Error: Please enter valid integers")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

else:
    print("Division result:", result)

finally:
    print("Program execution completed")
