import sqlite3

### Connecting to database #################
connection = sqlite3.connect("tog_v3.db")
cursor = connection.cursor()
############################################

stationList = []
for row in cursor.execute("""SELECT Delstrekning.stasjon1, Delstrekning.stasjon2
FROM Delstrekning
NATURAL JOIN HarDelstrekning
NATURAL JOIN Banestrekning
WHERE Banestrekning.navn = 'Nordlandsbanen'"""):
    print(cursor.fetchall())
    stationList.append(cursor.fetchone())

print(stationList)


### Adding changes ###
connection.commit()
connection.close()
######################