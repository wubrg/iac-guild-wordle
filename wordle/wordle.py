from termcolor import colored
from wordle.errors import DictionaryError, GuessError
import os.path
import random


class Wordle:
    def __init__(self, max_attempts, dictionary, solution=""):
        self.attempts = []
        self.solved = False
        self.dictionary_file = dictionary
        self.dictionary = self.__validate_dictionary(self.dictionary_file)
        self.solution = self.__generate_solution(solution)
        self.max_attempts = self.__set_max_attempts(max_attempts)
        self.solution_partial_matches = []
        self.solution_perfect_matches = ["0", "1", "2", "3", "4"]

    def attempts_left(self):
        return self.max_attempts - len(self.attempts)

    def guess(self, word):
        word = word.lower().strip()
        result = self.__check_solution(word)
        self.display_state()

        if self.attempts_left() < 1:
            self.__game_over(
                colored(
                    f"Looks like you lose! The correct answer was {self.solution}! Thanks for playing :)",
                    "red",
                )
            )

        return result

    def display_state(self):
        print(f"partial_matches: {self.solution_partial_matches}")
        print(f"perfect_matches: {self.solution_perfect_matches}")
        self.__print_guesses()

    def __validate_dictionary(self, path):
        if not os.path.exists(path):
            raise DictionaryError("Dictionary does not exist")

        dictionary = open(path, "r").readlines()
        clean_dictionary = [i.strip() for i in dictionary]

        if len(clean_dictionary) == 0:
            raise DictionaryError("Dictionary is empty")

        return clean_dictionary

    def __add_partial_match_char(self, char):
        if char in self.solution_partial_matches:
            return True

        self.solution_partial_matches.append(char)

    def __add_perfect_match_char(self, char, index):
        self.__add_partial_match_char(char)
        self.solution_perfect_matches[index] = char

    def __build_guess_colors(self, guess):
        match_color = "green"
        partial_match_color = "yellow"
        no_match_color = "grey"
        guess_colors = []
        for i, c in enumerate(guess):
            if guess[i] == self.solution[i]:
                guess_colors.append(match_color)
                self.__add_partial_match_char(c)
                self.__add_perfect_match_char(c, i)
            elif guess[i] in self.solution:
                guess_colors.append(partial_match_color)
                self.__add_partial_match_char(c)
            else:
                guess_colors.append(no_match_color)

        return guess_colors

    def __print_guess(self, guess):
        colors = self.__build_guess_colors(guess)

        guess_string = (
            colored(guess[0], colors[0])
            + colored(guess[1], colors[1])
            + colored(guess[2], colors[2])
            + colored(guess[3], colors[3])
            + colored(guess[4], colors[4])
        )
        print(guess_string)

    def __print_guesses(self):
        for attempt in self.attempts:
            self.__print_guess(attempt)

    def __set_max_attempts(self, num_attempts):
        max = int(num_attempts)
        if max < 1:
            print("Using the default max attempt setting of 5")
            return 5

        return max

    def __generate_solution(self, solution=""):
        if (solution == "") or (solution == None):
            return self.__random_solution()

        if len(solution) > 5:
            print(
                "solution provided is too long! We are generating random wordle for you..."
            )
            return self.__random_solution()

        return solution.lower()

    def __random_solution(self):
        return random.choice(self.dictionary).lower().strip()

    def __already_guessed(self, word):
        if word in self.attempts:
            print(
                colored(f"You already tried guessing {word}... Please try again", "red")
            )
            return True
        return False

    def __guess_correct_length(self, word):
        if len(word) == 5:
            return True

        print(
            colored(
                f"Your guess {word} must be 5 characters... Please try again", "red"
            )
        )
        return False

    def __guess_is_word(self, word):
        if word.lower().strip() in self.dictionary:
            return True

        print(
            colored(
                f"Your guess {word} must be a valid word from our dictionary: {self.dictionary_file}",
                "red",
            )
        )
        return False

    def __valid_guess(self, guess):
        if self.__already_guessed(guess):
            return False

        if not self.__guess_correct_length(guess):
            return False

        if not self.__guess_is_word(guess):
            return False

        return True

    def __check_solution(self, guess):
        if self.__valid_guess(guess):
            self.attempts.append(guess)
            if guess.lower() == self.solution.lower():
                self.__game_over(
                    colored("You Win! Thanks for playing :)", "green"), True
                )
                return True
            return False

        return False

    def __game_over(self, message, success=False):
        if success:
            self.solved = True
            print(message)
        else:
            print(message)
