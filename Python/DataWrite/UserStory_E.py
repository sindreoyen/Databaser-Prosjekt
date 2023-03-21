import sqlite3

### Connecting to database #################
connection = sqlite3.connect("tog_v2.db")
cursor = connection.cursor()
############################################

#navn = input("Skriv inn navnet ditt: ")
#epost = input("Skriv inn din epost: ")
#mobilnr = input("Skriv inn ditt mobilnummer: ")

##try:
#cursor.execute("""INSERT INTO Kunde
    #VALUES(NULL, ?,?,?)""",
#(navn, epost, mobilnr))
##except Exception:
    ##print("Something went wrong")
cursor.execute("SELECT * FROM Kunde")
kunder = cursor.fetchall()
print(kunder)

### Adding changes ###
connection.commit()
connection.close()
######################