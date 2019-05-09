from models import User, Meta_Col
from base import app, db, session_scope
from flask import render_template, jsonify, request, redirect


@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()
    with session_scope() as session:
        session.add(User('team', 'Bob_Jones', 'bob@gmail.com', 'Bob', 'Jones', 'cell', '123-123-4567', ''))
        session.add(User('team','Joe_Doe', 'eat@joes.com', 'Joe', 'Doe', '', '', 'test123'))
        session.add(User('team','Jane_Doe', 'jane@gmail.com', 'Jane', 'Doe', '', '', ''))
        session.add(Meta_Col('testcat','sub', 'testcol', 'test', 'testing 123', 'test, test, and test'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    users = db.session.query(User).all()
    col = db.session.query(Meta_Col).all()

    merge = [users, col]
    print(merge)
    return render_template("test.html", list = merge)

@app.route("/index1")
def index1():
    return render_template("index1.html")


if __name__ == "__main__":
    app.run()


            