from pathlib import Path
import sqlite3

values = (
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29),
)

with sqlite3.connect(Path.home() / "test_db.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute("""
        CREATE TABLE Roster(
            Name TEXT,
            Species TEXT,
            Age INT
        );"""
    )
    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)
    query = "SELECT * FROM Roster;"  # Создаём запрос
    results = cursor.execute(query)  # Выполняем запрос
    print(results.fetchall())  # Выводим запрос
    '''Обновите поле Name записи JadziaDax, чтобы оно содержало
    значение EzriDax.'''
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax';")
    query = "SELECT * FROM Roster;"  # Создаём запрос
    results = cursor.execute(query)  # Выполняем запрос
    print(results.fetchall())  # Выводим запрос
    '''Выведите значения Name и Age для всех строк данных, у
    которых поле Species содержит значение Bajoran.'''
    cursor.execute( "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';")
    for row in cursor.fetchall(): 
        print(row)
