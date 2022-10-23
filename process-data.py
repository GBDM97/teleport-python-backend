import sqlite3

conn = sqlite3.connect('teleport-db.sqlite')
cur = conn.cursor()
aCount = 1

cur.execute('SELECT * FROM AdminDs ORDER BY id DESC LIMIT 1')
aCountLimit = cur.fetchone()[0]

while True:
    cur.execute('SELECT salary FROM Cities WHERE id_adminD = (?)', (aCount, ))
    unknown = cur.fetchone()[0]
    aCount = aCount + 1
    if aCount > aCountLimit: break

    print(unknown,type(unknown))

    # salary DECIMAL UNIQUE,
    # leisureS DECIMAL UNIQUE,
    # safetyS DECIMAL UNIQUE,
    # businessFredomS DECIMAL UNIQUE,
    # costOfLivingS DECIMAL UNIQUE,
    # travelConnectivityS DECIMAL UNIQUE,
    # educationS DECIMAL UNIQUE,
