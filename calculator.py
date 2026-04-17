# def calculator(a, b = None, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#     print("================================================")

# calculator(1) #only a
# calculator(1,2) #no args and kwargs
# calculator(1,2,3)
# calculator(1,2,3,4)
# calculator(1,2,3,4,{5: 6,7: 8,9: 10})


def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 -num2
    elif operator == "*":
        result = num1 *num2
    elif operator == "/":
        if float(num2) != 0:
            result = float(num1) / float(num2)
        else:
            print("Invalid operation")

    print("Result: ", result)
calculator()
