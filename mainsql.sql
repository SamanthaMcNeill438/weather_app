-- Create Table
CREATE TABLE Weather(
    City TEXT NOT NULL,
    Min_Temp REAL NOT NULL,
    Max_Temp REAL NOT NULL,
    Avg_Temp REAL NOT NULL, 
    Humidity REAL NOT NULL,
    PRIMARY KEY (City)
);

-- Add record to the database
INSERT INTO Weather(City, Min_Temp, Max_Temp, Avg_Temp, Humidity)
VALUES (?, ?, ?, ?, ?);

-- Search database for record where city == user specified value
SELECT Min_Temp, Max_Temp, Avg_Temp, Humidity 
FROM Weather 
WHERE City LIKE ?;

-- Search database for record to update data
UPDATE Weather
SET Min_Temp = ?, Max_Temp = ?, Avg_Temp = ?, Humidity = ?
WHERE City LIKE ?;

-- Search database for record where city == user specified value, if found delete record
DELETE FROM Weather WHERE City LIKE ?;