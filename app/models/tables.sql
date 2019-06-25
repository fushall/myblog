DROP TABLE IF EXISTS Article;
CREATE TABLE IF NOT EXISTS Article(
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	title_type VARCHAR(32),
	abstract TEXT,
	abstract_type VARCHAR(32),
	text TEXT,
	text_type VARCHAR(32),
	visible BOOLEAN,
	accessible BOOLEAN,
	create_at TIMESTAMP WITH TIME ZONE
);
