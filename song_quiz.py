rhymes = {"1": "Soothe My Soul",
          "2": "Precious",
          "3": "Personal Jesus",
          "4": "Enjoy the Silence",
          "5": "Cover Me",
          "6": "Strangelove",
          "7": "Things You Said",
          "8": "Never Let Me Down Again",
          "9": "Behind the Wheel",
          "10": "Wrong"
}

n = input("Введите число: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Не найдено.")
