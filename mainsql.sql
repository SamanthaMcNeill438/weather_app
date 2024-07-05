CREATE DATABASE WEATHERAPP


DROP TABLE Weather



CREATE TABLE Weather(
    City nvarchar(50) not null,
    Min_Temp float not null,
    Max_Temp float not null,
    Avg_Temp float not null, 
    Humidity float not null,
    CONSTRAINT [PK_City] PRIMARY KEY ([City])
)


CREATE PROCEDURE sp_addData(
    @City nvarchar
    @Min_Temp float
    @Max_Temp float
    @Avg_Temp float
    @Humidity float
    AS
    INSERT INTO Weather(City, Min_Temp, Max_Temp, Avg_Temp, Humidity)
    VALUES Weather(City, Min_Temp, Max_Temp, Avg_Temp, Humidity)
) 