import sqlite3

conn = sqlite3.connect('teleport-db.sqlite')
cur = conn.cursor()
line = 1
aCount = 1
count = 1
salary = 0
leisureS = 0 
safetyS = 0 
businessFredomS = 0 
costOfLivingS = 0 
travelConnectivityS = 0 
educationS = 0 
aCountLimit = cur.execute('''SELECT * FROM adminDs ORDER BY ID DESC LIMIT 1''')

while True:
    while True:
        try:
            cur.execute('SELECT id_adminD,salary,leisureS,safetyS,businessFredomS,costOfLivingS,travelConnectivityS,educationS FROM Cities WHERE id = (?)', (line, ))
            out = cur.fetchone()
            data = str(out)
            data = data.strip(')').strip('(').split(',')
            print(type(data))
            id = data[0]
            num = data[1]
            if id == aCount:
                try:
                    l[0] = l[0] + 1 
                    l[1] = l[1] + data[1]
                    l[2] = l[2] + data[2]
                    l[3] = l[3] + data[3]
                    l[4] = l[4] + data[4]
                    l[5] = l[5] + data[5]
                    l[6] = l[6] + data[6]
                    l[7] = l[7] + data[7]
                except:
                    l = [ count , salary , leisureS , safetyS , businessFredomS , costOfLivingS , travelConnectivityS , educationS ] 
            count = count + 1 
        except Exception as err: print(err); break

        listCount = l[0]
        l[0] = l[1] / listCount
        l[1] = l[2] / listCount
        l[2] = l[3] / listCount
        l[3] = l[4] / listCount
        l[4] = l[5] / listCount
        l[5] = l[6] / listCount
        l[6] = l[7] / listCount
        l[7] = l[8] / listCount

        cur.execute('''INSERT INTO adminDs (salary , leisureS , safetyS , businessFredomS , costOfLivingS , travelConnectivityS , educationS) VALUES (?,?,?,?,?,?,?)''', (salary , leisureS , safetyS , businessFredomS , costOfLivingS , travelConnectivityS , educationS) )

    aCount = aCount + 1
    if aCount > aCountLimit: break


    # salary DECIMAL UNIQUE,
    # leisureS DECIMAL UNIQUE,
    # safetyS DECIMAL UNIQUE,
    # businessFredomS DECIMAL UNIQUE,
    # costOfLivingS DECIMAL UNIQUE,
    # travelConnectivityS DECIMAL UNIQUE,
    # educationS DECIMAL UNIQUE,
