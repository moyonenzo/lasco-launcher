debug:
	python3 .

install:
	python3 -m pip install -r requirements.txt

build:
	pyinstaller __main__.py

clean:
	sudo rm -rf build && sudo rm -rf dist && sudo rm -f __main__.spec