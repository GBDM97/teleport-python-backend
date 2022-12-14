import urllib.request, urllib.parse, urllib.error
import json
import sqlite3

conn = sqlite3.connect('teleport-db.sqlite')
cur = conn.cursor()
ur = urllib.request.urlopen('http://api.teleport.org/api/urban_areas/')
js = json.loads(ur.read().decode())
idented = json.dumps(js["_links"]["ua:item"], indent=4)

cur.executescript('''
DROP TABLE IF EXISTS Cities;
DROP TABLE IF EXISTS AdminDs;
DROP TABLE IF EXISTS Countries;
DROP TABLE IF EXISTS Comparisons;
DROP TABLE IF EXISTS GraphTypes;

CREATE TABLE Cities (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    city STRING,
    salary DECIMAL,
    leisureS DECIMAL,
    safetyS DECIMAL,
    businessFredomS DECIMAL,
    costOfLivingS DECIMAL,
    travelConnectivityS DECIMAL,
    educationS DECIMAL,
    id_adminD INTEGER
);

CREATE TABLE AdminDs (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    adminD STRING,
    id_country INTEGER
);

CREATE TABLE Countries (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    country STRING UNIQUE
);

CREATE TABLE Comparisons (
    id_city INTEGER,
    id_city2 INTEGER,
    orderP INTEGER UNIQUE,
    id_graphType INTEGER,
    PRIMARY KEY (id_city , id_city2)
);

CREATE TABLE GraphTypes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    graphType INTEGER UNIQUE
);

''')



c=95
di = dict()
renderLimit = 267

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
        try:
            city = json.dumps(js["_links"]["ua:item"][c]["name"])
            city = city.strip('"').split(',')[0]
            link = json.dumps(js["_links"]["ua:item"][c]["href"]).strip('"')

            ur = urllib.request.urlopen(link)
            js2 = json.loads(ur.read().decode())
            country = json.dumps(js2["_links"]["ua:countries"][0]["name"]).strip('"')
            try:
                adminD = json.dumps(js2["_links"]["ua:admin1-divisions"][0]["name"]).strip('"')
            except:
                adminD = country
            ur = urllib.request.urlopen(link + 'salaries')
            js2 = json.loads(ur.read().decode())
            salary = json.dumps(js2["salaries"][45]["salary_percentiles"]["percentile_50"])
            print(json.dumps(js2["salaries"][45]["job"]["id"]))

            ur = urllib.request.urlopen(link + 'scores')
            js2 = json.loads(ur.read().decode())
            leisureS = json.dumps(js2["categories"][14]["score_out_of_10"])
            safetyS = json.dumps(js2["categories"][7]["score_out_of_10"])
            businessFredomS = json.dumps(js2["categories"][6]["score_out_of_10"])
            costOfLivingS = json.dumps(js2["categories"][1]["score_out_of_10"])
            travelConnectivityS = json.dumps(js2["categories"][4]["score_out_of_10"])
            educationS = json.dumps(js2["categories"][9]["score_out_of_10"])

            # print(json.dumps(js2["categories"][14]))
            # print(json.dumps(js2["categories"][7]))
            # print(json.dumps(js2["categories"][6]))
            # print(json.dumps(js2["categories"][1]))
            # print(json.dumps(js2["categories"][4]))
            # print(json.dumps(js2["categories"][9]))

            
            try:
                cur.execute('SELECT id FROM Countries WHERE country = (?)', (country, ))
                id_country = cur.fetchone()[0]
            except Exception as err:
                print(err)
                cur.execute('''INSERT INTO Countries (country) VALUES (?)''',(country, ) )
                cur.execute('SELECT id FROM Countries WHERE country = (?)', (country, ))
                id_country = cur.fetchone()[0]
            try:
                cur.execute('SELECT id FROM AdminDs WHERE adminD = (?)', (adminD, ))
                id_adminD = cur.fetchone()[0]
            except Exception as err:
                print(err)
                cur.execute('''INSERT INTO AdminDs (adminD , id_country) VALUES (? , ?)''',(adminD, id_country) )
                cur.execute('SELECT id FROM AdminDs WHERE adminD = (?)', (adminD, ))
                id_adminD = cur.fetchone()[0]
            cur.execute('''INSERT OR IGNORE INTO Cities (city , salary , leisureS , safetyS , businessFredomS , costOfLivingS, travelConnectivityS, educationS, id_adminD) VALUES (? , ? , ? , ? , ? , ? , ? , ? , ?)''',(city, salary, leisureS, safetyS, businessFredomS, costOfLivingS, travelConnectivityS, educationS, id_adminD))              
            print(city, salary, leisureS, safetyS, businessFredomS, costOfLivingS, travelConnectivityS, educationS, id_adminD)
            c = c + 1
            if c >= (renderLimit): break
        except Exception as err:
            print (err)
            break
                
conn.commit()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')







