CREATE TABLE IF NOT EXISTS BlogUser (
	id INTEGER PRIMARY KEY,
	username TEXT,
	password TEXT,
	nickname TEXT,
	created_at DATE,
	user_type TEXT
);

CREATE TABLE IF NOT EXISTS UserInfo(
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  nickname TEXT
);


CREATE TABLE IF NOT EXISTS UserArticle(
	id INTEGER PRIMARY KEY,
	user_id INTEGER,
	article_id INTEGER
);

CREATE TABLE IF NOT EXISTS Article(
	id INTEGER PRIMARY KEY,
	title TEXT,
	article_type TEXT,
	article_state SMALLINT,  -- 1: shown, 0: hidden, 2: deleted, 3: locked
	content TEXT,
	content_type TEXT,  -- 0: html, 1: markdown
	category_id INTEGER,
	create_at DATE,
	update_at DATE
);
CREATE TABLE IF NOT EXISTS ArticleCategory(
	id INTEGER PRIMARY KEY,
	name TEXT,
	state SMALLINT,
	created_at DATE
	update_at DATE

);
-- DROP TABLE IF EXISTS BlogUser;
-- DROP TABLE IF EXISTS UserInfo;
-- DROP TABLE IF EXISTS UserArticle;
