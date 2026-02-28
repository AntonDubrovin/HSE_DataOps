include .env

dev.install:
	pip install yoyo-migrations psycopg2-binary

db.migration.new:
	yoyo new ./migrations -d $(DATABASE_URL)

db.migrate:
	yoyo apply ./migrations -d $(DATABASE_URL)

db.rollback:
	yoyo rollback ./migrations -d $(DATABASE_URL)
