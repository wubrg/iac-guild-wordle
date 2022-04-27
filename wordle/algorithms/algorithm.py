import wordle


class Algorithm:
    def __init__(self, wordle):
        self.wordle = wordle
        self.name = "Default"

    def suggest(self):
        print(f"{self.name} suggests you guess `{self.__educated_guess()}`")
        return "guess"
