from yoyo import step

step(
    "ALTER TABLE users ADD COLUMN lastname VARCHAR(100)",
    "ALTER TABLE users DROP COLUMN lastname"
)
