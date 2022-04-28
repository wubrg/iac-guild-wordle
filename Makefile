
init:
	brew install pip3
	brew install python3
	brew install pyenv
	chmod +x ./play_wordle.py

setup:
	pip3 install -r ./requirements.txt

play:
	python3 ./play_wordle.py

check:
	python3 -m black ./play_wordle.py --check
	python3 -m black ./wordle/wordle.py --check
	python3 -m black ./wordle/errors.py --check
	python3 -m black ./wordle/algorithms/algorithm.py --check
	python3 -m black ./wordle/algorithms/blasty.py --check
	python3 -m black ./wordle/algorithms/browny.py --check

check_format:
	python3 -m black ./play_wordle.py --diff --color
	python3 -m black ./wordle/wordle.py --diff --color
	python3 -m black ./wordle/errors.py --diff --color
	python3 -m black ./wordle/algorithms/algorithm.py --diff --color
	python3 -m black ./wordle/algorithms/blasty.py --diff --color
	python3 -m black ./wordle/algorithms/browny.py --diff --color

format:
	python3 -m black ./play_wordle.py
	python3 -m black ./wordle/wordle.py
	python3 -m black ./wordle/errors.py
	python3 -m black ./wordle/algorithms/algorithm.py
	python3 -m black ./wordle/algorithms/blasty.py
	python3 -m black ./wordle/algorithms/browny.py
