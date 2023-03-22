import sqlite3
import LocalData


### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

epost = input("Skriv inn din epost som du er oppgitt med hos oss: ")

cursor.execute("SELECT epost FROM Kunde")
eposter_temp = cursor.fetchall()
eposter = []

for row in eposter_temp:
    eposter.append(row[0])
if epost not in eposter:
    raise Exception("Epost finnes ikke i kunderegisteret")

1679475912

### Adding changes ###
connection.commit()
connection.close()
######################