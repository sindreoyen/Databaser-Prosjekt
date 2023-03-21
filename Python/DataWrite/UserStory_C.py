import sqlite3

### Connecting to database #################
connection = sqlite3.connect("Tog-db.db")
cursor = connection.cursor()
############################################

stasjon = input("Hvilken stasjon ønsker du å velge? ")
ukedag = input("Hvilken ukedag ønsker du å sjekke togreiser for? ")

##cursor.execute("SELECT * FROM Jernbanestasjon")
##Jernbanestasjoner = cursor.fetchall()
##print(Jernbanestasjoner)

try: 
    cursor.execute("""SELECT DISTINCT ruteID
FROM Togrute 
NATURAL JOIN (SELECT KjørerStrekning.ruteID, KjørerStrekning.delstrekningID, Delstrekning.stasjon1, Delstrekning.stasjon2
FROM KjørerStrekning
NATURAL JOIN Delstrekning
WHERE Delstrekning.stasjon1 = 'Trondheim S' OR Delstrekning.stasjon2 = 'Trondheim S'
)
NATURAL JOIN GårPåUkedag
WHERE GårPåUkedag.navn = 'man'"""
)
    togruter = cursor.fetchall()
    print(togruter)
except Exception:
    print("Ugyldig input")


##ukedagDict = {
    ##"mandag": "man",
    ##"tirsdag": "tir",
    ##"onsdag": "ons",
    ##"torsdag": "tor",
    ##"fredag": "fre",
    ##"lørdag": "lør",
    ##"søndag": "søn"
##}

##if not ukedag.lower() in ukedagDict:
    ##raise Exception("Ugyldig ukedag")


### Adding changes ###
connection.commit()
connection.close()
######################