import LocalData
import Validators

print("Ikke laget ferdig")

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

user: tuple = None
while user == None:
    email = input("Hei! Vennligst skriv eposten til brukeren du er registrert med: ")
    user = Validators.fetchUser(email=email, connection=connection)




### Cose the connection ####################
connection.close()
############################################