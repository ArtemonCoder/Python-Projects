def f():
    age = input("Введите возраст: ")
    age = int(age)
    if age <= 20:
        print("You're so young!")
    elif 20 < age <= 32:
        print("You're in the best age!")
    elif 32 < age <= 50:
        print("В самом рассвете сил и красоты!")
    else:
        print("Age doesn't matter. You look better within years!")
f()    
