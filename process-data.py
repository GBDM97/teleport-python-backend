import sqlite3

conn = sqlite3.connect('teleport-db.sqlite')
cur = conn.cursor()
line = 0
aCount = 1
cur.execute('''SELECT id FROM adminDs ORDER BY ID DESC LIMIT 1''')
out = cur.fetchone()
aCountLimit = int(out[0])
l = [0,0,0,0,0,0,0,0]

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
    cur.execute('''INSERT INTO adminDs (mediumSalary , leisureS , safetyS , businessFredomS , costOfLivingS , travelConnectivityS , educationS) VALUES (?,?,?,?,?,?,?) WHERE id = (?)''', (l[0] , l[1] , l[2] , l[3] , l[4] , l[5] , l[6])(aCount) )
    l = [0,0,0,0,0,0,0,0]
    line = 0
    aCount = aCount + 1
    if aCount > aCountLimit: break
conn.commit()

    # salary DECIMAL UNIQUE,
    # leisureS DECIMAL UNIQUE,
    # safetyS DECIMAL UNIQUE,
    # businessFredomS DECIMAL UNIQUE,
    # costOfLivingS DECIMAL UNIQUE,
    # travelConnectivityS DECIMAL UNIQUE,
    # educationS DECIMAL UNIQUE,
