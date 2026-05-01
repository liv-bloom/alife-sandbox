.PHONY: test all run

test:
	python3 -m unittest discover -p "test_*.py"

run:
	python3 demo_all.py

all: test run
