import os
import pandas as pd

# This function get the city files in the excel sheet
def Get_Cityfiles(name):
    print(name)
    # Read file to dataframe
    file_path = os.path.join(".", "static/dataset", "city_file_list.csv")
    df = pd.read_csv(file_path)
    print(file_path)
    if name != "all":
        # Initialize comparison list
        ilist = ["my_map", "leastStore", "TopStore", "review", "words", "rating", "categories"]
        
        # Query dataframe to filter the city
        result_df = df.loc[(df["City"] == city)]  
        
        # Initialize dictionary to store result
        r_list = {}

        # Loop thru result dataframe & comparison list to get format records into a dictionary list
        for i, rw in result_df.iterrows():
            for x in ilist:
                if x in rw.New_Name:
                    r_list[x] = rw.File_Path
    else:
        print("unique cities")
        # Initialize list to store unique cities
        r_list = []    
        r_list = df.City.unique()

    return r_list