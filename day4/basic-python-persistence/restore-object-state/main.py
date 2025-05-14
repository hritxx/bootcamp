import pickle

class Game:
    def __init__(self):
        self.level = 1
        self.score = 0

    def save_state(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.__dict__, f)

    def load_state(self, filename):
        with open(filename, "rb") as f:
            self.__dict__ = pickle.load(f)

game = Game()
game.level = 3
game.score = 1500
game.save_state("game.sav")

new_game = Game()
new_game.load_state("game.sav")
print(new_game.__dict__)