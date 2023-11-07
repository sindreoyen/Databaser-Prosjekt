import sqlite3
from typing import Tuple, List
import datetime

def findStationsDirection(connection: sqlite3.Connection) -> Tuple[str, str, int]:
    """
    Returns a tuple containing the start station name, end station name and whether 
    the main direction is being followed (1 for True, 0 for False)
    """
    cursor = connection.cursor()
    stations = cursor.execute("""SELECT Delstrekning.stasjon1, Delstrekning.stasjon2
                                FROM Delstrekning
                                NATURAL JOIN HarDelstrekning
                                NATURAL JOIN Banestrekning
                                WHERE Banestrekning.navn = 'Nordlandsbanen'""").fetchall()

    station_dict = {}
    for station1, station2 in stations:
        if station1 not in station_dict:
            station_dict[station1] = []
        if station2 not in station_dict:
            station_dict[station2] = []
        station_dict[station1].append(station2)
        station_dict[station2].append(station1)

    start_station = ""
    end_station = ""

    print("\n\n# VELG STASJONER #")
    print("- Stasjoner: ", list(station_dict.keys()), " -")

    while start_station == "":
        station_input = input("Velg startstasjon: ")
        if station_input in station_dict:
            start_station = station_input
        else:
            print("OBS! Stasjonen eksisterer ikke. Velg på nytt.")

    while end_station == "" or start_station == end_station:
        station_input = input("Velg endestasjon: ")
        if station_input in station_dict:
            end_station = station_input
        else:
            print("OBS! Stasjonen eksisterer ikke. Velg på nytt.")

    with_main_dir = 0 if end_station == "Trondheim S" or start_station == "Bodø" else 1

    def find_index() -> int:
        prev_station = start_station
        attempt_index = 0
        while prev_station != end_station:
            try:
                next_station = station_dict[prev_station][attempt_index]
                prev_station = next_station
            except IndexError:
                print("Error checking stations")
            if next_station == end_station:
                return attempt_index
            if next_station == "Trondheim S":
                return 1

    if with_main_dir == -1:
        with_main_dir = find_index()
    
    return start_station, end_station, with_main_dir

def getTogruteWithDir(connection: sqlite3.Connection, dir: int) -> List[int]:
    """Gets all togrute ids with the given direction"""
    cursor = connection.cursor()
    togrute_ids = cursor.execute(
        "SELECT ruteID from Togrute WHERE medHovedRetning = ?", (dir,)
    ).fetchall()

    return [row[0] for row in togrute_ids]

def getTimeString(unixTime: int) -> str:
    """Returns a string of the time from a unix timestamp"""
    return datetime.datetime.utcfromtimestamp(unixTime).time().strftime("%H:%M")