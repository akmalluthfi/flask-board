import sqlite3
import click
from flask import current_app, g
import psycopg


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


@click.command("init-db")
def init_db_command():
    conn = psycopg.connect(
        host=current_app.config["DB_HOST"],
        dbname=current_app.config["DB_DATABASE"],
        user=current_app.config["DB_USERNAME"],
        password=current_app.config["DB_PASSWORD"],
        port=current_app.config["DB_PORT"],
    )

    cur = conn.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS posts;
        """
    )
    cur.execute(
        """
        CREATE TABLE posts (
            id serial PRIMARY KEY,
            created DATE DEFAULT CURRENT_DATE,
            author TEXT NOT NULL,
            message TEXT NOT NULL
        );
        """
    )

    conn.commit()
    cur.close()
    conn.close()
    click.echo("You successfully initialized the database!")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def get_pg_db_conn():
    conn = psycopg.connect(
        host=current_app.config["DB_HOST"],
        dbname=current_app.config["DB_DATABASE"],
        user=current_app.config["DB_USERNAME"],
        password=current_app.config["DB_PASSWORD"],
        port=current_app.config["DB_PORT"],
    )
    return conn
