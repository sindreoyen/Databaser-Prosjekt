import LocalData
import Validators
import G_methods.seats
import G_methods.coupes
import Utilities

print("Ikke laget ferdig")

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

user: tuple = None
while user == None:
    email = input("Hei! Vennligst skriv eposten til brukeren du er registrert med: ")
    user = Validators.fetchUser(email=email, connection=connection)
print(user)

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
    G_methods.coupes.orderCoupe(connection=connection)
    
else:
    print("Noe feil har skjedd, vennligst kjør programmet på nytt og sjekk din input.")


### Cose the connection ####################
connection.commit()
connection.close()
############################################