
init:
	brew install pyenv
	chmod +x ./play_wordle.py

setup:
	pip3 install -r ./requirements.txt

play:
	python3 ./play_wordle.py

check:
	python3 -m black ./play_wordle.py --check
	python3 -m black ./wordle/wordle.py --check
	python3 -m black ./wordle/algorithms/algorithm.py --check
	python3 -m black ./wordle/algorithms/blast.py --check

check_format:
	python3 -m black ./play_wordle.py --diff --color
	python3 -m black ./wordle/wordle.py --diff --color
	python3 -m black ./wordle/algorithms/algorithm.py --diff --color
	python3 -m black ./wordle/algorithms/blast.py --diff --color

format:
	python3 -m black ./play_wordle.py
	python3 -m black ./wordle/wordle.py
	python3 -m black ./wordle/algorithms/algorithm.py
	python3 -m black ./wordle/algorithms/blast.py
