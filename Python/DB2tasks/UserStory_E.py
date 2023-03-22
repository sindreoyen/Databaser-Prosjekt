import LocalData

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

navn = ""
epost = ""
mobilnr = ""

while navn == "":
    navn = input("Skriv inn navnet ditt: ")
while epost == "" and '@' not in epost:
    epost = input("Skriv inn din epost: ")
while mobilnr == "":
    mobilnr = input("Skriv inn ditt mobilnummer: ")

try:
    cursor.execute("""INSERT INTO Kunde
    VALUES(NULL, ?,?,?)""",
    (navn, epost, mobilnr))
    print("Takk,", navn + "! Din bruker er blitt opprettet.")
except Exception:
    print("Beklager,", navn + ".", "Noe gikk galt under opprettelse av kunde, vennligst prøv igjen.")

### Adding changes ###
connection.commit()
connection.close()
######################