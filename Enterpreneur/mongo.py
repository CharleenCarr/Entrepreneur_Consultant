from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://admin:admin123@janie-test-vcn3t.mongodb.net/test?retryWrites=true")
db = client.consultant

def Get_Region_Population():
    df = pd.DataFrame.from_records(db.population.find( { "Year": 2018, "Hierarchy": "Region", "Category": "Population" }, {'_id': 0} ))
    df["Percentage"] = (df["Population"] / df["Population"].sum()) * 100

    return df


def Get_Cities():
    rlist = db.list.distinct("City")
    return rlist

def GetList_by_City(name):
    df = pd.DataFrame.from_records(db.list.find({ "City": name }, {"_id": 0, "City": 1, "File": 1, "File_Path": 1}))
    return df


# # Default home page rendering html & data pass to it
# @app.route('/')
# def index():
#     mars_data = db.mars.find_one()
#     return render_template('index.html', mars = mars_data)

# # When button was clicked on the home page, this will 
# # call the scrape function to get the updates
# @app.route('/scrape')
# def scrape():
#     # print("scraping function")
#     # Call scrape function and get data return from it
#     mars = db.mars
#     data = scrapin.scrape_mars()

#     # Update mongodb with new data
#     mars.update(
#         {},
#         data,
#         upsert=True
#     )

#     return redirect("/", code=302)