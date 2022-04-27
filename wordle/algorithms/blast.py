from wordle.algorithms.algorithm import Algorithm


class BlastAlgorithm(Algorithm):
    def __init__(self, wordle):
        Algorithm.__init__(self, wordle)
        self.suggestion = self.__educated_guess()
        self.name = "Blasty"

    def suggest(self):
        print(f"{self.name} suggests you guess `{self.__educated_guess()}`")
        return self.suggestion

    def __educated_guess(self):
        return "blast"
