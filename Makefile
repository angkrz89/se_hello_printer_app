.PHONY: test

deps:
		pip install -r requirements.txt; \
		pip install -r test_requirements.txt

test:
	  PYTHONPATH=. py.test
	  PYTHONPATH=. py.test --verbose -s

run:
		python main.py

lint: # noqa
		flake8 hello_world test
