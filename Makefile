brain-games: # Запустить программу brain-games
	poetry run brain-games


brain-even: # Запустить программу brain-games
	poetry run brain-even


install: # Install programs
	poetry install


build: # build
	poetry build


publish: # Публикация репозитория
	poetry publish --dry-run


package-install: # package-install
	python3 -m pip install --user dist/*.whl


lint: # Linter
	poetry run flake8 brain_games
