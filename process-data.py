import sqlite3

conn = sqlite3.connect('teleport-db.sqlite')
cur = conn.cursor()
line = 0
aCount = 1
cur.execute('''SELECT id FROM adminDs ORDER BY ID DESC LIMIT 1''')
out = cur.fetchone()
aCountLimit = int(out[0])
l = [0,0,0,0,0,0,0,0]

cur.executescript(''' 
DROP TABLE IF EXISTS AdminDsMediumScores;
DROP TABLE IF EXISTS CountriesMediumScores;

CREATE TABLE AdminDsMediumScores (
    id_adminD INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    mediumSalary DECIMAL,
    leisureS DECIMAL,
    safetyS DECIMAL,
    businessFredomS DECIMAL,
    costOfLivingS DECIMAL,
    travelConnectivityS DECIMAL,
    educationS DECIMAL,
    id_country INTEGER
);
CREATE TABLE CountriesMediumScores (
    id_country INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    mediumSalary DECIMAL,
    leisureS DECIMAL,
    safetyS DECIMAL,
    businessFredomS DECIMAL,
    costOfLivingS DECIMAL,
    travelConnectivityS DECIMAL,
    educationS DECIMAL
);
''')

while True:
    while True:
        line = line + 1
        try:
            cur.execute('SELECT id_adminD,salary,leisureS,safetyS,businessFredomS,costOfLivingS,travelConnectivityS,educationS FROM Cities WHERE id = (?)', (line, ))
            data = cur.fetchone()
            id = int(data[0])
            if id == aCount:
                l[0] = l[0] + 1 
                l[1] = l[1] + data[1]
                l[2] = l[2] + data[2]
                l[3] = l[3] + data[3]
                l[4] = l[4] + data[4]
                l[5] = l[5] + data[5]
                l[6] = l[6] + data[6]
                l[7] = l[7] + data[7]
        except Exception as err: print(err); break
        
    listCount = l[0]
    if listCount == 0: listCount = 1
    l[0] = l[1] / listCount
    l[1] = l[2] / listCount
    l[2] = l[3] / listCount
    l[3] = l[4] / listCount
    l[4] = l[5] / listCount
    l[5] = l[6] / listCount
    l[6] = l[7] / listCount
    l[7] = 0
    cur.execute('SELECT id_country from AdminDs WHERE id = (?)', (aCount,))
    data = cur.fetchone()
    id_country = int(data[0])
    cur.execute('''INSERT INTO adminDsMediumScores (mediumSalary , leisureS , safetyS , businessFredomS , costOfLivingS , travelConnectivityS , educationS, id_country) VALUES (?,?,?,?,?,?,?,?)''', (l[0] , l[1] , l[2] , l[3] , l[4] , l[5] , l[6], id_country) )
    l = [0,0,0,0,0,0,0,0]
    line = 0
    aCount = aCount + 1
    if aCount > aCountLimit: break

line = 0
aCount = 1
cur.execute('''SELECT id FROM Countries ORDER BY ID DESC LIMIT 1''')
out = cur.fetchone()
aCountLimit = int(out[0])
l = [0,0,0,0,0,0,0,0]

while True:
    while True:
        line = line + 1
        try:
            cur.execute('SELECT id_adminD,mediumSalary,leisureS,safetyS,businessFredomS,costOfLivingS,travelConnectivityS,educationS,id_country FROM AdminDsMediumScores WHERE id_adminD = (?)', (line, ))
            data = cur.fetchone()
            id = int(data[8])
            if id == aCount:
                l[0] = l[0] + 1 
                l[1] = l[1] + data[1]
                l[2] = l[2] + data[2]
                l[3] = l[3] + data[3]
                l[4] = l[4] + data[4]
                l[5] = l[5] + data[5]
                l[6] = l[6] + data[6]
                l[7] = l[7] + data[7]
        except Exception as err: print(err); break
        
    listCount = l[0]
    if listCount == 0: listCount = 1
    l[0] = l[1] / listCount
    l[1] = l[2] / listCount
    l[2] = l[3] / listCount
    l[3] = l[4] / listCount
    l[4] = l[5] / listCount
    l[5] = l[6] / listCount
    l[6] = l[7] / listCount
    l[7] = 0
    # cur.execute('SELECT id_country from AdminDs WHERE id = (?)', (aCount,))
    # data = cur.fetchone()
    # id_country = int(data[0])
    cur.execute('''INSERT INTO CountriesMediumScores (mediumSalary , leisureS , safetyS , businessFredomS , costOfLivingS , travelConnectivityS , educationS) VALUES (?,?,?,?,?,?,?)''', (l[0] , l[1] , l[2] , l[3] , l[4] , l[5] , l[6]) )
    l = [0,0,0,0,0,0,0,0]
    line = 0
    aCount = aCount + 1
    if aCount > aCountLimit: break

conn.commit()
