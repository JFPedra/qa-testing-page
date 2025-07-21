.PHONY: install run test

install:
	poetry install --no-root

run:
	poetry run flask --app app.routes run --debug

test:
	poetry run pytest  --html=report.html --self-contained-html
