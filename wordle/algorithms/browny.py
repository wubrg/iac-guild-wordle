from wordle.algorithms.algorithm import Algorithm
import random
import numpy as np


class BrownAlgorithm(Algorithm):
    def __init__(self, wordle):
        super().__init__(wordle)
        self.name = "Browny"
        self.wordle = wordle

    def suggest(self):
        guess = self.__educated_guess()
        print(f"{self.name} suggests you guess `{guess}`")
        return guess

    def __educated_guess(self):
        return random.choice(self.get_perfect_matching_words())

    def get_partial_matching_words(self):
        options = []
        [options.append(i) for i in self.wordle.dictionary if self.partial_match(i)]

        if len(options) == 0:
            return self.wordle.dictionary

        return np.unique(options)

    def partial_match(self, word):
        matches = []
        for char in self.wordle.solution_partial_matches:
            if char in word:
                matches.append(True)
            else:
                matches.append(False)

        if len(matches) == 0:
            return False

        if matches.count(True) == len(self.wordle.solution_partial_matches):
            return True

        return False

    def get_perfect_matching_words(self):
        perfects = []
        partials = self.get_partial_matching_words()
        [perfects.append(word) for word in partials if self.perfect_match(word)]

        if len(perfects) == 0:
            return partials

        return perfects

    def perfect_match(self, word):
        matches = []
        matches_known = 5
        for index, char in enumerate(self.wordle.solution_perfect_matches):
            if char in ["0", "1", "2", "3", "4"]:
                matches_known -= 1

            if word[index] == char:
                matches.append(True)
            else:
                matches.append(False)

        if len(matches) == 0:
            return False

        if matches.count(True) == matches_known:
            return True

        return False
