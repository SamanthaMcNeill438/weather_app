DROP TABLE Weather

CREATE TABLE Weather(
    City nvarchar(50) not null,
    Min_Temp float not null,
    Max_Temp float not null,
    Avg_Temp float not null, 
    Humidity float not null,
    CONSTRAINT [PK_City] PRIMARY KEY ([City])
)