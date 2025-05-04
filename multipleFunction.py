class multipleFunctions():
    def oddEven():
        num=int(input("Enter number: "))
        if (num%2==1):
            print("Odd number")
            message="Odd number"
        else:
            print("Even number")
            message="Even number"
        return message

    def BMI():
        BMI=int(input("Enter BMI index: "))
        if (BMI<18.5):
            print("Underweight")
            message="Underweight"
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        else:
            print("Overweight")
            message="Overweight"
        return message