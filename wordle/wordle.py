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
        result = self.__check_solution(word)
        self.display_state()

        if self.attempts_left() < 1:
            self.__game_over("Looks like you lose! Thanks for playing :)")

        return result

    def display_state(self):
        self.__print_results()

    def __print_results(self):
        print(self.attempts)

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
            self.__game_over("You Win! Thanks for playing :)")

        if guess in self.attempts:
            print(f"You already tried guessing {guess}... Please try again")
            return False

        self.attempts.append(guess)
        return False

    def __game_over(self, message):
        self.display_state()
        exit(message)
