import os.path
import pandas as pd
import json
import numpy as np

class DataManager():
    def __init__(self, filename, url):
        self.prevDay = None
        self.currentDay = None
        self.df = self.loadData(filename, url)
        self.daynr = 0
        self.maxDays = len(self.getStartIDByDay())
        print(self.maxDays)

    def loadData(self, filename, url):
        basepath = "./data/bike"
        filepath = os.path.join(basepath, filename)
        try:
            df = pd.read_json(filepath, orient="split")
            return df
        except ValueError:
            print("No file found, loading from url")
            df = pd.read_json(url)
            to_drop = [ "ended_at",
                "duration",
                "start_station_name",
                "start_station_description",
                "end_station_id",
                "end_station_name",
                "end_station_description",
                "end_station_latitude",
                "end_station_longitude"]
            df.drop(columns=to_drop, inplace=True)
            df.to_json(filepath, orient="split")
            return df
            
    def informationOnDay(self, dayInMonth):
        stationsByDay = self.getStartIDByDay()
        locations = self.getLocations()
        daysInformation = stationsByDay.iloc[dayInMonth]
        
        stationOccurences = {}
        for key in locations.keys():
            stationOccurences[key] = 0
        
        for val in daysInformation:
            stationOccurences[val]+=1
           

        return stationOccurences

    def nextDay(self):
        self.prevDay = self.currentDay
        self.currentDay = self.informationOnDay(self.daynr)
        self.daynr += 1
        self.daynr %= self.maxDays


    def getCoordinates(self):
        locations = self.getLocations()
        stations = locations.keys()
        x = np.array([locations[station]["start_station_latitude"] for station in stations])
        y = np.array([locations[station]["start_station_longitude"] for station in stations])
        return x,y

    def minAndMaxCoordinates(self):
        minlat, maxlat = self.df["start_station_latitude"].min(), self.df["start_station_latitude"].max()
        minlong, maxlong = self.df["start_station_longitude"].min(), self.df["start_station_longitude"].max()
        return minlat, maxlat, minlong, maxlong
        

    def getLocations(self):
        return self.df.groupby("start_station_id")["start_station_latitude", "start_station_longitude"].mean().to_dict('index')

    def getStartIDByDay(self):
        return self.df.groupby(self.df["started_at"].dt.day)["start_station_id"].apply(list)
    
    def getDay(self):
        return (self.daynr-1)%self.maxDays+1






