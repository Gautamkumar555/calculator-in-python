def calculator():
    while True:
        a = input("Enter operation name \n add \n sub \n mul \n div \n: ").lower()
        b = float(input("Enter 1st number: "))
        c = float(input("Enter 2nd number: "))

        if a == "add":
            print("Addition of your numbers is", b + c)
        elif a == "sub":
            print("Subtraction of your numbers is", b - c)
        elif a == "mul":
            print("Multiplication of your numbers is", b * c)
        elif a == "div":
            print("Division of your numbers is", b / c)
        else:
            print("Enter valid operators only")

        repeat = input("Do you want to perform another calculation? (yes/no): ")
        if repeat.lower() != "yes":
            print("Thanks for using Gautam's calculator!")
            break

# Start the calculator
calculator()
