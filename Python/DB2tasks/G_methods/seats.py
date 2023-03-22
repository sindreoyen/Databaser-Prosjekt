import sqlite3

def orderSeat(connection: sqlite3.Connection, ids: list,
              startStation: str, endStation: str, 
              withMainDir: int):
    cursor = connection.cursor()

    ## Find available trains
    idx = 0
    trainMap = {}
    for id in ids:
        statement = """
        SELECT DATE(Tf.dato, 'unixepoch', 'localtime'), 
        TIME(KS.tidStasjon1, 'unixepoch', 'localtime'), 
        TIME(KS.tidStasjon2, 'unixepoch', 'localtime'), 
        Ds.stasjon1, Ds.stasjon2, Tf.navn, Tf.dato
        FROM 
        Togruteforekomst Tf 
        LEFT OUTER NATURAL JOIN KjørerStrekning KS
        LEFT OUTER NATURAL JOIN Delstrekning Ds
        WHERE Tf.ruteID=?"""
        postfix = ("1" if withMainDir == 1 else "2")
        statement += " AND Ds.stasjon" + postfix + "='" + startStation + "'"
        statement += "\nORDER BY Tf.dato, KS.tidStasjon" + postfix + " DESC"

        for row in cursor.execute(statement, (id,)):
            date = row[0]
            startTime = row[1 if withMainDir else 2]
            name = row[5]
            print(date + ": Toget,", name, "går fra", startStation, "kl:", startTime)



    statement = """
    SELECT Sete.seteNR, VognIOppsett.vognNR, Tf.navn, Tf.ruteID,
    DATE(Tf.dato, 'unixepoch', 'localtime'), 
    ds.stasjon1, ds.stasjon2, ds.delstrekningID
    FROM
    Sete LEFT OUTER NATURAL JOIN
    Vogn LEFT NATURAL JOIN 
    VognIOppsett NATURAL JOIN
    VognOppsett LEFT OUTER NATURAL JOIN
    Togrute LEFT OUTER NATURAL JOIN
    TogruteForekomst Tf LEFT OUTER NATURAL JOIN
    Delstrekning ds
    ORDER BY Tf.dato, Sete.seteNR, VognIOppsett.vognNR ASC
    """
    allSeats: list = []
    for row in cursor.execute(statement):
        allSeats.append(row)
    print(allSeats.count())