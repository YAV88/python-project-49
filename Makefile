brain-games: # Run brain-games
	poetry run brain-games


brain-even: # Run game 'The Even'
	poetry run brain-even


brain-calc: # Run game 'Calculate'
	poetry run brain-calc


brain-gcd: # Run game 'GCD'
	poetry run brain-gcd


brain-progression: # Run game 'Arithmetic progression'
	poetry run brain-progression


brain-prime: # Run game 'Arithmetic progression'
	poetry run brain-prime


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
