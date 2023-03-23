import sqlite3
import LocalData


### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

stations: list = []
for row in cursor.execute("SELECT navn FROM Jernbanestasjon"):
    stations.append(row[0])

print("Tilgjengelige stasjoner: " + str(stations))
station = ""
while station not in stations:
    station: str = input("Hvilken stasjon ønsker du å velge?: ")


weekdayDict: dict = {
    "mandag": "man",
    "tirsdag": "tir",
    "onsdag": "ons",
    "torsdag": "tor",
    "fredag": "fre",
    "lørdag": "lør",
    "søndag": "søn"
}
weekday: str = ""
while True:
    try: 
        weekday = input("Hvilken ukedag ønsker du å sjekke togreiser for?: ")
        weekday = weekdayDict[weekday.lower()]
        break
    except: 
        print("Feil format!")
        print("Forventet: " + str(list(weekdayDict.keys())))


try:
    for row in cursor.execute("""SELECT DISTINCT ruteID
                      FROM Togrute 
                      NATURAL JOIN (SELECT KjørerStrekning.ruteID, KjørerStrekning.delstrekningID, Delstrekning.stasjon1, Delstrekning.stasjon2
                                   FROM KjørerStrekning
                                   NATURAL JOIN Delstrekning
                                   WHERE Delstrekning.stasjon1 = ? OR Delstrekning.stasjon2 = ?)
                      NATURAL JOIN GårPåUkedag
                      WHERE GårPåUkedag.navn = ?""",
                   (station, station, weekday)):
        print(row)
        print("##### TODO: Fiks bedre output her")
    
except Exception:
    print("Ugyldig input")


### Adding changes ###
#connection.commit()
connection.close()
######################