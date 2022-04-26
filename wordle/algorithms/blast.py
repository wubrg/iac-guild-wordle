from wordle.algorithms.algorithm import Algorithm


class BlastAlgorithm(Algorithm):
    def __init__(self, wordle):
        Algorithm.__init__(self, wordle)

    def suggest(self):
        return "blast"
