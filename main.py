import math

end_condition = False

while not end_condition:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    delta = b * b - 4 * a * c

    if delta > 0:
        x1 = round((- b + math.sqrt(delta)) / 2 * a, 2)
        x2 = round((- b - math.sqrt(delta)) / 2 * a, 2)

        print("Wynik: x1 = {}, x2 = {}".format(x1, x2))

    elif delta == 0:
        x0 = round(- b / 2 * a, 2)
        print("Wynik: x0 = {}".format(x0))

    else:
        print("Program nie liczy pierwiastków zespolonych!")

    print("Kontynuować?")
    c = input("[T/N] ")
    c = c.upper()

    if c == "N":
        end_condition = True
        break
