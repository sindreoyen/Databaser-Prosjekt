from lib2to3.pgen2.pgen import DFAState
from multiprocessing import connection
import sqlite3
import LocalData


### Connecting to database #################
##connection = LocalData.getDBConnection()
connection = sqlite3.connect("b&e.db")
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


## Find departure time and arrival 

cursor.execute("""SELECT MAX(MAX(KjørerStrekning.tidStasjon1), MAX(KjørerStrekning.tidStasjon2)), MIN(MIN(KjørerStrekning.tidStasjon1), MIN(KjørerStrekning.tidStasjon2))
FROM Kundeordre
NATURAL Join Kunde
NATURAL JOIN Togrute
NATURAL JOIN Setebillett
NATURAL JOIN SetebillettIOrdre
NATURAL JOIN Delstrekning
NATURAL JOIN KjørerStrekning """)
times = cursor.fetchall()
departureTime = times[0][1]
arrivalTime = times [0][0]
print(departureTime, arrivalTime)
### Adding changes ###
connection.commit()
connection.close()
######################