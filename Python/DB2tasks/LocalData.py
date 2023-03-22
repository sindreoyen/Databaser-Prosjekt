import datetime
import sqlite3
import pathlib

### Data
path: str = str(pathlib.Path(__file__).parent.resolve())

## DB name
dbName = "tog_db.db"

def getDBConnection() -> sqlite3.Connection:
    """Fetches a connection to the database"""
    connection = sqlite3.connect(dbName)
    hasData: bool = __checkDBHasData(connection=connection)
    if hasData:
        print("DB exists with data")
        return connection
    else:
        print("Creating new DB")
        return __fillDB(connection=connection)


## Dates
currentDate = datetime.datetime.now()

### Utilities - SQL helper
def __checkDBHasData(connection: sqlite3.Connection) -> bool:
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM Delstrekning")
        return True
    except Exception:
        return False
    
def __fillDB(connection: sqlite3.connect) -> sqlite3.Connection:
    setup = "Tog-SQL.sql"
    inserts = ["Inserts.sql"] #Seter.sql
    __execScript(sqlite_file=setup, connection=connection)
    for script in inserts:
        __execScript(sqlite_file=script, connection=connection)
    return connection

def __execScript(sqlite_file: str, connection: sqlite3.Connection):
    prefix: str = path + "/SQL/"
    with open(prefix + sqlite_file, 'r') as sql_file:
        sql_script = sql_file.read()

    cursor = connection.cursor()
    cursor.executescript(sql_script)
    connection.commit()