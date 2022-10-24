install: .env
	poetry install

start:
	poetry run python3 app/bot.py

lint:
	poetry run flake8 app

test:
	poetry run pytest .

coverage-report:
	poetry run pytest --cov=app --cov-report xml

show-test-coverage:
	poetry run pytest --cov=app

.env:
	@test ! -f .env && cp .env.example .env
