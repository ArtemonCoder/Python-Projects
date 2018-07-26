rock = []
pop = []

def collect_songs():
    song = "Укажите песню."
    ask = "Введите р(рок) или п(поп). Введите X для выхода."

    while True:
        genre = input(ask)
        if genre == "X":
            break

        if genre == "р":
            rk = input(song)
            rock.append(rk)

        elif genre == "п":
            cy = input(song)
            pop.append(cy)

        else:
            print("Повторите ввод!")
    print(rock)
    print(pop)

collect_songs()     
