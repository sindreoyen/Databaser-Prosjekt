import sqlite3
import LocalData


### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

stasjon = input("Hvilken stasjon ønsker du å velge? ")
ukedag_temp = input("Hvilken ukedag ønsker du å sjekke togreiser for? ")

ukedagDict = {
    "mandag": "man",
    "tirsdag": "tir",
    "onsdag": "ons",
    "torsdag": "tor",
    "fredag": "fre",
    "lørdag": "lør",
    "søndag": "søn"
}

ukedag = ukedagDict[ukedag_temp.lower()]

try:
    cursor.execute("""SELECT DISTINCT ruteID
                      FROM Togrute 
                      NATURAL JOIN (SELECT KjørerStrekning.ruteID, KjørerStrekning.delstrekningID, Delstrekning.stasjon1, Delstrekning.stasjon2
                                   FROM KjørerStrekning
                                   NATURAL JOIN Delstrekning
                                   WHERE Delstrekning.stasjon1 = ? OR Delstrekning.stasjon2 = ?)
                      NATURAL JOIN GårPåUkedag
                      WHERE GårPåUkedag.navn = ?""",
                   (stasjon, stasjon, ukedag))
    togruter = cursor.fetchall()
    print(togruter)
except Exception:
    print("Ugyldig input")


### Adding changes ###
#connection.commit()
connection.close()
######################