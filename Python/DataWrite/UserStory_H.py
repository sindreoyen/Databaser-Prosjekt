import sqlite3

### Connecting to database #################
connection = sqlite3.connect("tog_v3.db")
cursor = connection.cursor()
############################################

epost = input("Skriv inn din epost som du er oppgitt med hos oss: ")

cursor.execute("SELECT epost FROM Kunde")
eposter_temp = cursor.fetchall()
eposter = []

for row in eposter_temp:
    eposter.append(row[0])
print(eposter)

if epost not in eposter:
    raise Exception("Epost finnes ikke i kunderegisteret")
else:
    print("Good")

### Adding changes ###
connection.commit()
connection.close()
######################