try:
    a = input("Введите число: ")
    b = input("Ещё одно: ")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Ошибся? Ну всё! Ща математичка придёт тебя хоронить!")
