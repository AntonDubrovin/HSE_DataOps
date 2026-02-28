from yoyo import step

step(
    "CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL)",
    "DROP TABLE users"
)
