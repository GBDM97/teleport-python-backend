from textwrap import indent
import urllib.request, urllib.parse, urllib.error
import json
import sqlite3
import re

conn = sqlite3.connect('teleport-db.sqlite')
cur = conn.cursor()
ur = urllib.request.urlopen('http://api.teleport.org/api/urban_areas/')
js = json.loads(ur.read().decode())
idented = json.dumps(js["_links"]["ua:item"], indent=4)

cur.executescript('''
DROP TABLE IF EXISTS Cities;
DROP TABLE IF EXISTS AdminD;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Comparison;
DROP TABLE IF EXISTS GraphType;

CREATE TABLE Cities (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    city STRING UNIQUE,
    salary DECIMAL UNIQUE,
    leisureS DECIMAL UNIQUE,
    safetyS DECIMAL UNIQUE,
    businessFredomS DECIMAL UNIQUE,
    costOfLivingS DECIMAL UNIQUE,
    salaryScoreIndex DECIMAL UNIQUE,
    id_adminD INTEGER,
    link STRING UNIQUE
);

CREATE TABLE AdminD (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    adminD STRING UNIQUE,
    adminDIndex DECIMAL UNIQUE,
    id_country INTEGER
);

CREATE TABLE Country (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    country STRING UNIQUE,
    countryMediumIndex DECIMAL UNIQUE
);

CREATE TABLE Comparison (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    id_city INTEGER,
    id_city2 INTEGER,
    orderP INTEGER UNIQUE,
    id_graphType INTEGER
);

CREATE TABLE GraphType (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    graphType INTEGER UNIQUE
);

''')



c=0
di = dict()
rLimit = 2

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
        try:
            city = json.dumps(js["_links"]["ua:item"][c]["name"])
            city = city.strip('"').split(',')[0]
            link = json.dumps(js["_links"]["ua:item"][c]["href"]).strip('"')

            ur = urllib.request.urlopen(link)
            js2 = json.loads(ur.read().decode())
            country = json.dumps(js2["links"]["ua:countries"][0]["name"])
            adminD = json.dumps(js2["links"]["ua:admin1-divisions"][0]["name"])

            ur = urllib.request.urlopen(link + 'salary')
            js2 = json.loads(ur.read().decode())
            salary = json.dumps(js2["salaries"][45]["salary_percentiles"]["percentile_50"])
            print(json.dumps(js2["salaries"][45]["job"]["id"]))

            ur = urllib.request.urlopen(link + 'scores')
            js2 = json.loads(ur.read().decode())
            leisureS = json.dumps(js2["categories"][14]["score_out_of_10"])
            safetyS = json.dumps(js2["categories"][7]["score_out_of_10"])
            businessFredomS = json.dumps(js2["categories"][6]["score_out_of_10"])
            costOfLivingS = json.dumps(js2["categories"][1]["score_out_of_10"])
             

            print(json.dumps(js2["salaries"][45]["job"]["id"]))

            cur.execute('''INSERT OR REPLACE INTO Cities (city , salary) VALUES (? , ?)''',(city , salary) )              
            c = c + 1
            if c == (rLimit): break
        except:
            break
                

conn.commit()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')







