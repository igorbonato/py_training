while True:
    num1 = int(input("please tell me one number: "))
    num2 = int(input("please tell me another number: "))
    if num1 > num2:
        print(num1, "is bigger than", num2)
        break
    elif num2 > num1:
        print(num2, "is bigger than", num1)
        break
    else:
        print("u need to tell me differents numbers okay?")
