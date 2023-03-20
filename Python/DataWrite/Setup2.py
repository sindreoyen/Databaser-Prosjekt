import sqlite3
import Statements

### Connecting to database #################
connection = sqlite3.connect("Tog-db.db")
cursor = connection.cursor()
############################################

for j in range(2,5):
    for i in range(1,13):
        try:
            cursor.execute(Statements.sete, j, i)
        except Exception:
            print("Already added stations")




### Adding changes ###
connection.commit()
connection.close()
######################