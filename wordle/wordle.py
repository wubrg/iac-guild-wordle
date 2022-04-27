from termcolor import colored


class Wordle:
    def __init__(self, max_attempts, dictionary, solution=""):
        self.attempts = []
        self.solved = False
        self.solution = self.__generate_solution(solution)
        self.max_attempts = self.__set_max_attempts(max_attempts)

    def attempts_left(self):
        return self.max_attempts - len(self.attempts)

    def guess(self, word):
        word = word.lower()

        if self.check_if_already_guessed(word):
            return False

        self.attempts.append(word)
        result = self.__check_solution(word)
        self.display_state()

        if self.attempts_left() < 1:
            self.__game_over("Looks like you lose! Thanks for playing :)")

        return result

    def check_if_already_guessed(self, word):
        if word in self.attempts:
            print(f"You already tried guessing {word}... Please try again")
            self.display_state()
            return True
        return False

    def display_state(self):
        self.__print_guesses()

    def __build_guess_colors(self, guess):
        match_color = "green"
        partial_match_color = "yellow"
        no_match_color = "grey"
        guess_colors = []
        for i, c in enumerate(guess):
            if guess[i] == self.solution[i]:
                guess_colors.append(match_color)
            elif guess[i] in self.solution:
                guess_colors.append(partial_match_color)
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
        return "blast".lower()

    def __check_solution(self, guess):
        # Check matching characters then validate if answer is correct
        if guess == self.solution:
            self.solved = True
            self.__game_over("You Win! Thanks for playing :)")

        return False

    def __game_over(self, message):
        self.display_state()
        exit(message)
