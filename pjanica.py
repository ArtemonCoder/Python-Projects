from random import shuffle

class Card:
    suits = ["пик",
             "червей",
             "бубей",
             "треф"]
    values = [None, None,"2", "3", "4", "5", "6", "7",
              "8", "9","10", "валет(а)", "дам(у)",
              "корол(ь/я)", "туз(а)"]

    def __init__(self, v,s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
            return False
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
         return self.values[self.value] + " " + self.suits[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
                                  
    def rm_card(self):
        if len(self.cards) == 0:
             return
        return self.cards.pop()
                                  
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("имя 1-го игрока: ")
        name2 = input("имя 2-го игрока: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print("Поехали!")
        response = None
        while len(cards) >= 2:
            response = input('Нажмите Х для выхода. Нажмите любую другую клавишу для начала игры.')
            if response == 'Х':
                break
            player1_card = self.deck.rm_card()
            player2_card = self.deck.rm_card()
            print("{} кладет {}, а {} кладет {}.".format(self.player1.name, player1_card, self.player2.name, player2_card))
            if player1_card > player2_card:
                self.player1.wins += 1
                print("{} забирает карты".format(self.player1.name))
            else:
                self.player2.wins += 1
                print("{} забирает карты".format(self.player2.name))
        print("Игра окончена. {} выиграл!".format(self.winner(self.player1, self.player2)))

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "Ничья!"

game = Game()
game.play_game()
