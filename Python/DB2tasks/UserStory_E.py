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
while mobilnr == "" and len(mobilnr) != 8:
    mob: str = input("Skriv inn ditt mobilnummer: ")
    try: mobilnr = int(mob)
    except: print("Mobilnummeret må være et tall.")

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