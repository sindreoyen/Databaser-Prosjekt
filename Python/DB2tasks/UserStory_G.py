import LocalData
import Validators
import G_methods.seats
import G_methods.coupes
import Utilities

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

## Check if any users exist in db
cursor.execute("SELECT * FROM Kunde")
if cursor.fetchone() == None:
    print("Ingen brukere er registrert i databasen. Du må registrere en bruker først i brukerhistorie E.")
    exit()

user: tuple = None
while user == None:
    email = input("Hei! Vennligst skriv eposten til brukeren du er registrert med: ")
    user = Validators.fetchUser(email=email, connection=connection)

def orderCoupe():
    print("Coupe")
options = ["k", "s"]

choice = ""
while choice.lower() not in options:
    choice = input("Vennligst skriv inn K dersom du ønsker sovekupé, eller S dersom du ønsker et sete\n[K / S]: ")

if choice.lower() == "s":
    res = Utilities.findStationsDirection(connection=connection)
    ids = Utilities.getTogruteWithDir(connection=connection, dir=res[2])
    G_methods.seats.orderSeat(connection=connection, ids=ids,
                              startStation=res[0], endStation=res[1],
                              withMainDir=res[2], customerID=user[0])
elif choice.lower() == "k":
    res = Utilities.findStationsDirection(connection=connection)
    ids = Utilities.getTogruteWithDir(connection=connection, dir=res[2])
    G_methods.coupes.orderCoupe(connection=connection, ids=ids,
                              startStation=res[0], endStation=res[1],
                              withMainDir=res[2], customerID=user[0])
else:
    print("Noe feil har skjedd, vennligst kjør programmet på nytt og sjekk din input.")


### Cose the connection ####################
connection.commit()
connection.close()
############################################