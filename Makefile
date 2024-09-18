venv:
	python -m venv .venv
	. .venv/bin/activate

install: venv
	pip install -r requirements.txt

build: install
	pyinstaller --onefile --distpath=. wcc.py

clean:
	rm -rf .venv
	rm -rf __pycache__

.PHONY: venv install build clean
