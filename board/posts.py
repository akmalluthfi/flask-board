from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from board.database import get_db, get_pg_db_conn

bp = Blueprint("posts", __name__)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_pg_db_conn()
            cur = db.cursor()
            cur.execute(
                """
                    INSERT INTO posts (author, message) 
                    VALUES (%s, %s);
                """,
                (author, message),
            )
            db.commit()
            cur.close()
            db.close()

            return redirect(url_for("posts.posts"))

    return render_template("posts/create.html")


@bp.route("/posts")
def posts():
    db = get_pg_db_conn()
    cur = db.cursor()

    cur.execute("SELECT author, message, created FROM posts ORDER BY created DESC;")
    posts = cur.fetchall()

    cur.close()
    db.close()

    return render_template("posts/posts.html", posts=posts)
