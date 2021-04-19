while True:
    pi = 3.1416
    try:
        radius = float(input("whats ur radius: "))
    except ValueError:
        print("just numbers ur ignorant slut")
        continue
    else:
        circle_area = (radius * radius) * pi
        print('the area of ur circle is %.2f' % circle_area)
        break
