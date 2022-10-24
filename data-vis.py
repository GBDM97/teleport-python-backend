import sqlite3

conn = sqlite3.connect('teleport-db.sqlite')
cur = conn.cursor()
cur.execute('''INSERT INTO GraphTypes (graphType) VALUES (?)''',('black-white', ) )
cur.execute('''INSERT INTO GraphTypes (graphType) VALUES (?)''',('colored', ) )

c1 = int(("118/171").split('/'))
c2 = int(("118/36").split('/'))
c3 = int(("118/125").split('/'))

cur.execute('''INSERT INTO Comparisons (id_city,id_city2,orderP,id_graphType) VALUES (?,?,?,?)''',(c1[0], c1[1], 3, 1 ) )
cur.execute('''INSERT INTO Comparisons (id_city,id_city2,orderP,id_graphType) VALUES (?,?,?,?)''',(c2[0], c2[1], 2, 2 ) )
cur.execute('''INSERT INTO Comparisons (id_city,id_city2,orderP,id_graphType) VALUES (?,?,?,?)''',(c3[0], c3[1], 1, 2 ) )

conn.commit()

print('boraaa meo')




