# Definierte Variablen:
run = True

operation = input("Welche Operation (+, -, *, /) soll durchgeführt werden: ")
if operation == "q":
        run = False
else:
    number1 = float(input("Gebe die erste Zahl ein: "))
    number2 = float(input("Gebe die zweite Zahl ein: "))


while(run):
    if operation == "+":
        print(number1 + number2)
    elif operation == "-":
        print(number1 - number2)
    elif operation == "*":
        print(number1 * number2)
    elif operation == "/":
        print(number1 / number2)
    else:
        print("Ungültige Operation...")

    operation = input("Welche Operation (+, -, *, /) soll durchgeführt werden, Bei q wird das Programm beendet. ")
    if operation == "q":
        run = False
    else:
        number1 = float(input("Gebe die erste Zahl ein: "))
        number2 = float(input("Gebe die zweite Zahl ein: "))