while True:
    metre_cent = float(input("just type 1 for metre or 2 for centimeter: "))
    if metre_cent == 1:
        metre = float(input("tell me ur met: "))
        print("ur metre in cm is: ", metre * 100)
        break
    elif metre_cent == 2:
        cent = float(input("tell me ur cent: "))
        print("ur cent in met is: ", cent / 100)
        break
    else:
        print("just type 1 or 2 ur fucking idiot".upper())
    continue
