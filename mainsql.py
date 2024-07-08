sql_create = """
CREATE TABLE Weather(
    City TEXT NOT NULL,
    Min_Temp REAL NOT NULL,
    Max_Temp REAL NOT NULL,
    Avg_Temp REAL NOT NULL, 
    Humidity REAL NOT NULL,
    PRIMARY KEY (City)
);"""

sql_insert = """
INSERT INTO Weather(City, Min_Temp, Max_Temp, Avg_Temp, Humidity)
VALUES (?, ?, ?, ?, ?);"""

sql_select = """SELECT Min_Temp, Max_Temp, Avg_Temp, Humidity 
FROM Weather 
WHERE City LIKE ?;"""

sql_update = """UPDATE Weather
SET Min_Temp = ?, Max_Temp = ?, Avg_Temp = ?, Humidity = ?
WHERE City LIKE ?;"""

sql_delete = """DELETE FROM Weather WHERE City LIKE ?;"""