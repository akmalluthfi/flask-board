DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
  id serial PRIMARY KEY,
  created DATE DEFAULT CURRENT_DATE,
  author TEXT NOT NULL,
  message TEXT NOT NULL
);