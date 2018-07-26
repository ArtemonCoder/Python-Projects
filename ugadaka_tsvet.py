colors = ["фиолетовый", "оранжевый", "синий"]
guess = input("Угадайте цвет: ")

if guess in colors:
    print("Вы угадали!")
else:
    print("Не угадали, давайте еще раз.")
    
guess2 = input("Угадайте цвет: ")

if guess2 in colors:
    print("Вы угадали!")
else:
    print("Не угадали, давайте еще раз.")

