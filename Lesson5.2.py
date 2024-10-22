while True:
    first_number = float(input("Введите первое число: "))
    operation = input("Введите действие (+, -, *, /): ")
    second_number = float(input("Введите второе число: "))
    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "*":
        print(first_number * second_number)
    elif operation == "/":
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("НА 0 ДЕЛИТЬ НЕЛЬЗЯ!")

    continue_calculation = input("Хотите продолжить? (y/n): ").lower()
    if continue_calculation == "n":
        print("Вычисление завершено.")
        break