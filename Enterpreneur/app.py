from models import User, Meta_Col
from base import app, db, session_scope
from flask import render_template, jsonify, request, redirect
import mongo 



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

# Dashboard
@app.route('/')
def home():
    return render_template("index.html")

#  Navigation button click will render city template
@app.route('/city')
def city():
    return render_template("city.html")

@app.route('/region')
def region():
    return render_template("region.html")

@app.route('/county')
def county():
    return render_template("county.html")

@app.route('/state')
def state():
    return render_template("state.html")
#---------------------------------------------------

@app.route("/names")
def names():
    """Return a list of city names."""
    rlist= mongo.Get_Cities()

    # Return a list of the column names 
    return jsonify(rlist)

@app.route('/select/<city>')
def select(city):
    # Read file to dataframe
    data = mongo.GetList_by_City(city)
    results = {
        # "city": data.City.values.tolist(),
        "file_path": data.File_Path.values.tolist(),
        # "file": data.File.values.tolist(),
    }
    
    return jsonify(results)
#---------------------------------------------------

@app.route("/population")
def population():
    data = mongo.Get_Region_Population()
    results = {
        "percent": data.Percentage.values.tolist(),
        "Name": data.H_Name.values.tolist(),
    }

    # Return a list of the column names (sample names)
    return jsonify(results )

#---------------------------------------------------
# ------------------------------------------------------    

# @app.route("/test")
# def test():
#     users = db.session.query(User).all()
#     col = db.session.query(Meta_Col).all()

#     merge = [users, col]
#     print(merge)
#     return render_template("test.html", list = merge)

# @app.route("/index1")
# def index1():
#     return render_template("index1.html")


if __name__ == "__main__":
    app.run()


            