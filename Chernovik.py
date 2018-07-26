al = ["1", "5", "666", "111", "228", "190"]
n = 0
while True:
    a = input("Угадай число или введи 'X' для выхода : ")
    if a == "X":
        break
    elif a in al:
        print("Вы угадали")
    elif a not in al:
        print("Вы не угадали")
