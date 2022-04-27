from wordle.wordle import Wordle
from wordle.algorithms.blasty import BlastAlgorithm
from wordle.algorithms.browny import BrownAlgorithm


def load_algorithm(name, wordle_game):
    if name.lower() == "blasty":
        return BlastAlgorithm(wordle_game)
    elif name.lower() == "browny":
        return BrownAlgorithm(wordle_game)
    else:
        return BlastAlgorithm(wordle_game)


def play_wordle(game, algorithm, automated=False):
    while game.attempts_left() and not game.solved > 0:
        if automated:
            guess = ""
        else:
            guess = input(
                """
                Please input your next guess.
                An empty string will let the chosen algorithm make its best guess.
                """
            )

        if guess == "":
            guess = algorithm.suggest()

        game.guess(guess)


def create_game(attempts, dictionary, solution=""):
    return Wordle(attempts, dictionary, solution)


if __name__ == "__main__":
    attempts = 5
    algorithm = "browny"
    automated = False
    dict = "/Users/adamwieberg/Downloads/five-letter-words-no-names.txt"
    # solution = 'blast'
    game = create_game(attempts, dict, "grass")
    assistant = load_algorithm(algorithm, game)
    play_wordle(game, assistant, automated)
