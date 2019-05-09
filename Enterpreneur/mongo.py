from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin123@janie-test-vcn3t.mongodb.net/test?retryWrites=true")
db = client.consultant


# # Get data from mongo & convert back to dataframe
# df = pd.DataFrame.from_records(db.crime.find({}, {'_id': 0 }))
# df

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