debug:
	python3 .

install:
	python3 -m pip install -r requirements.txt

build:
	pyinstaller __main__.py