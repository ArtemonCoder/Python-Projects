    """
    Попытка введения функции float
    :Параметр n: число.
    """
try:
    n=input("Введите число: ")
    n=float(n)
    print(float(n))
except ValueError:
    print("Ошибка ввода")
