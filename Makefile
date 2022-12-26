brain-games: # Запустить программу brain-games
	poetry run brain-games

install: # Install programs
	poetry install

build: # build
	poetry build

publish: #
	poetry publish --dry-run

package-install #
	python3 -m pip install --user dist/*.whl


