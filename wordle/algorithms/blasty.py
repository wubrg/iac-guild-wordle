from wordle.algorithms.algorithm import Algorithm


class BlastAlgorithm(Algorithm):
    def __init__(self, wordle):
        super().__init__(wordle)
        self.name = "Blasty"
        print("Hey, its Blasty!")

    def suggest(self):
        print(f"{self.name} suggests you guess `{self.__educated_guess()}`")
        return self.__educated_guess()

    def __educated_guess(self):
        return "blast"
