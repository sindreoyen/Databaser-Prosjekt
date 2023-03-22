import sqlite3

### Users
def fetchUser(email: str, connection: sqlite3.Connection) -> tuple:
    """Fetch user tuple tied to email. Prints a greeting."""
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM Kunde WHERE epost=" + "'" + email + "'"):
        print("Velkommen,", row[1] + "!")
        return row
    print("Det eksisterer ingen bruker med denne eposten.")
