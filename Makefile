brain-games: # Run brain-games
	poetry run brain-games


brain-even: # Run game 'Even'
	poetry run brain-even


brain-calc: # Run game 'Calc'
	poetry run brain-calc


install: # Install programs
	poetry install


build: # build
	poetry build


publish: # Run publish
	poetry publish --dry-run


package-install: # package-install
	python3 -m pip install --user dist/*.whl


lint: # Linter
	poetry run flake8 brain_games
