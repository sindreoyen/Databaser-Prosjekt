from lib2to3.pgen2.pgen import DFAState
import sqlite3
import LocalData


### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################


##Validate if epost exist in db
##epost = input("Skriv inn din epost som du er oppgitt med hos oss: ")

# cursor.execute("SELECT epost FROM Kunde")
# eposter_temp = cursor.fetchall()
# eposter = []

# for row in eposter_temp:
#     eposter.append(row[0])
# if epost not in eposter:
#     raise Exception("Epost finnes ikke i kunderegisteret")

##make station list

cursor.execute("""SELECT * from Kunde""")
kunde = cursor.fetchall()
print(kunde)
## Find departure time and arrival 

cursor.execute("""SELECT  MAX(MAX(KjørerStrekning.tidStasjon1), MAX(KjørerStrekning.tidStasjon2)) as ankomst, MIN(MIN(KjørerStrekning.tidStasjon1), MIN(KjørerStrekning.tidStasjon2)) as avgang
FROM Kundeordre
NATURAL Join Kunde
INNER JOIN TogruteForekomst USING (ruteID, dato)
NATURAL JOIN Togrute
NATURAL JOIN Setebillett
NATURAL JOIN BillettIOrdre
NATURAL JOIN SetebillettIOrdre
NATURAL JOIN Delstrekning
NATURAL JOIN KjørerStrekning
WHERE Kunde.epost = 'e.saetre@online.no'
GROUP BY ordreNR""")
# times = cursor.fetchall()
# departureTime = times[0][1]
# arrivalTime = times [0][0]
# print(departureTime, arrivalTime)
print(cursor.fetchall())

"""SELECT  MAX(MAX(KjørerStrekning.tidStasjon1), MAX(KjørerStrekning.tidStasjon2)) as ankomst, MIN(MIN(KjørerStrekning.tidStasjon1), MIN(KjørerStrekning.tidStasjon2)) as avgang
FROM Kundeordre
NATURAL Join Kunde
INNER JOIN TogruteForekomst USING (ruteID, dato)
NATURAL JOIN Togrute
NATURAL JOIN Setebillett
NATURAL JOIN BillettIOrdre
NATURAL JOIN SetebillettIOrdre
NATURAL JOIN Delstrekning
NATURAL JOIN KjørerStrekning
WHERE Kunde.epost = 'e@o.no'
GROUP BY ordreNR, vognID, seteNR"""
### Adding changes ###
connection.commit()
connection.close()
######################