try:
    number=int(input("Enter a number: "))
    print("The number is enetered",number)

except ValueError as ex:
    print("Exception", ex)
