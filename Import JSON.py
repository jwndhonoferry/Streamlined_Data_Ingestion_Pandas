# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:12:35 2020

@author: jiwandhono
"""
import requests
from sqlalchemy import create_engine
import pandas as pd
from configparser import ConfigParser
import psycopg2
import mysql.connector
import json
import matplotlib as plt
#kalau bisa pakai pandas
data_json = pd.read_json("example_2.json", orient = "index")

#pakai json karena memkai pandas tidak bisa
# data = json.load(open("data.json"))
# data2 = json.dumps(data)


try:
    # Load the JSON with orient specified
    #Try to change orient (values, column, records, except split)
    df = pd.read_json("example_2.json", orient = "index")
    
    # Plot total population in shelters over time
    data_sport = pd.DataFrame(df["sport"])
    data_maths = pd.DataFrame(df["maths"])
    #df.plot(x=columns, 
    #         y=row)
    # plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")
    
    
    
# =============================================================================
# Introduction to APIs
# =============================================================================
api_url = "https://api.yelp.com/v3/businesses/search"
api_key = "a"
params = {"term" : "cafe", "location" : "NYC"}
headers = {"Authorization": "Bearer {}".format(api_key)}
# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a data frame
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)
print(cafes.head())













