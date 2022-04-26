from wordle.wordle import Wordle
from wordle.algorithms.blast import BlastAlgorithm


def load_algorithm(name, wordle_game):
    if name.lower() == "default":
        return BlastAlgorithm(wordle_game)
    else:
        return BlastAlgorithm(wordle_game)


def play_wordle(game, algorithm):
    while not game.solved:
        guess = input(
            """
            Please input your next guess.
            An empty string will let the chosen algorithm make its best guess.
            """
        )
        print(f'your guess is: {guess}.')
        if guess == "":
            game.guess(algorithm.suggest)
        else:
            game.guess(guess)


def create_game(attempts, dictionary, solution=""):
    return Wordle(attempts, dictionary, solution)


if __name__ == "__main__":
    attempts = 5
    algorithm = "default"
    dict = "~/Downloads/five-letter-words-no-names.txt"
    game = create_game(attempts, dict)
    assistant = load_algorithm(algorithm, game)
    print(game.solution)
    play_wordle(game, assistant)
