class Calculator:
     
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2 
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
    
while True:
    print("\n-------------------------------------- Calculator Menu --------------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multipllication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting...")
        break

    try:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: ")) 
    except ValueError:
        print("Invalid Input Please enter correct input")
        continue

    calc = Calculator(a,b)

     
    if choice == "1":
        print(f"Addition = {calc.add()}")

    elif choice == "2":
        print(f"Subtract = {calc.subtract()}")
    
    elif choice == "3":
        print(f"Multiplication = {calc.multiply()}")

    elif choice == "4":
        print(f"Division = {calc.divide()}")

    else:
        print("Invalid Choice..")







