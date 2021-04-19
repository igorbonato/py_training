while True:
    degrees = int(input("type 1 for celsius\ntype 2 for fahrenheit\n"))
    if degrees == 1:
        celsius = float(input("tell me ur celsius degrees: "))
        celsius_conv = 32 + ((celsius/5) * 9)
        print("%.2f fahrenheit" % celsius_conv)
    elif degrees == 2:
        fahr = float(input("tell me ur fahrenheit degrees: "))
        fahr_conv = 5 * ((fahr-32) / 9)
        print("%.2f celsius" % fahr_conv)
    else:
        print("OMG u are a fucking dumbass")
