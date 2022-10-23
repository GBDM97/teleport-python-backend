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
    score DECIMAL UNIQUE,
    salaryScoreIndex DECIMAL UNIQUE,
    id_adminD INTEGER
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
cities = 'none'
di = dict()

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
        try:
            cities = json.dumps(js["_links"]["ua:item"][c]["name"])
            cities = cities.strip('"').split(',')[0]
            cur.execute('''INSERT OR REPLACE INTO Cities (city) VALUES (?)''',(cities,) )                
            c = c + 1
        except:
            break
conn.commit()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')







