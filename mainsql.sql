-- CREATE DATABASE WEATHERAPP
DROP TABLE Weather

-- Create Table
CREATE TABLE Weather(
    City nvarchar(50) not null,
    Min_Temp float not null,
    Max_Temp float not null,
    Avg_Temp float not null, 
    Humidity float not null,
    CONSTRAINT [PK_City] PRIMARY KEY ([City])
)

-- Add record to the database
CREATE PROCEDURE sp_addData(
    @City nvarchar(50),
    @Min_Temp float,
    @Max_Temp float,
    @Avg_Temp float,
    @Humidity float
    AS
    INSERT INTO Weather(City, Min_Temp, Max_Temp, Avg_Temp, Humidity)
    VALUES (@City, @Min_Temp, @Max_Temp, @Avg_Temp, @Humidity)
) 

-- Search database for record where city == user specifiied value
CREATE PROCEDURE sp_searchData(
    @City nvarchar(50)
    AS
        SELECT Min_Temp, Max_Temp, Avg_Temp, Humidity 
        FROM Weather 
        WHERE City LIKE @City
) 

-- Search database for record to update data
CREATE PROCEDURE sp_updateData(
    @City nvarchar(50),
    @Min_Temp float,
    @Max_Temp float,
    @Avg_Temp float,
    @Humidity float
    AS
    UPDATE Weather
    SET City = @City,
        Min_Temp = @Min_Temp,
        Max_Temp = @Max_Temp,
        Avg_Temp = @Avg_Temp,
        Humidity = @Humidity
    WHERE City LIKE @City
)


-- Search database for record where city == user specifiied value, if found delete record
CREATE PROCEDURE sp_deleteData(
    @City nvarchar(50)
    AS
    DELETE FROM Weather WHERE City LIKE @City
)

