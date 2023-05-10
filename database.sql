BEGIN TRANSACTION;

DROP TABLE IF EXISTS Travel;
DROP TABLE IF EXISTS Cab;
DROP TABLE IF EXISTS CabType;
DROP TABLE IF EXISTS Place;
DROP TABLE IF EXISTS Passenger;
DROP TABLE IF EXISTS Driver;




CREATE TABLE Passenger (
    PassengerID varchar(7) NOT NULL ,
    FirstName varchar(20) DEFAULT NULL,
    LastName varchar(20) DEFAULT NULL,
    ContactNumber varchar(40) DEFAULT NULL,
    Gender varchar(10) DEFAULT NULL,
    EmailID varchar(50) DEFAULT NULL,
    DateOfBirth varchar(12) DEFAULT NULL,
    PRIMARY KEY (PassengerID)

);

-- --------------------------------------------------------

CREATE TABLE Driver (
    DriverID varchar(7) DEFAULT NULL,
    FirstName varchar(20) DEFAULT NULL,
    LastName varchar(20) DEFAULT NULL,
    ContactNumber varchar(40) DEFAULT NULL,
    Gender varchar(10) DEFAULT NULL,
    EmailID varchar(50) DEFAULT NULL,
    Rating int DEFAULT NULL,
    DateOfBirth varchar(12) DEFAULT NULL,
    PRIMARY KEY (DriverID)

);

-- --------------------------------------------------------


CREATE TABLE CabType(
    ctype varchar(20) NOT NULL,
    Price FLOAT DEFAULT NULL ,
    WaitingPrice FLOAT DEFAULT NULL ,
    MaxPassenger INT NOT NULL,
    PRIMARY KEY(ctype)
);

-- --------------------------------------------------------



CREATE TABLE Cab(
    DriverID varchar(7) NOT NULL,
    CabID varchar(7) NOT NULL,
    ctype varchar(20) NOT NULL,
    Condition varchar(15) DEFAULT NULL,
    PRIMARY KEY (CabID),
    CONSTRAINT fk_DriverID_cab
    FOREIGN KEY (DriverID)
    REFERENCES Driver(DriverID),
    CONSTRAINT fk_ctype_cab
    FOREIGN KEY(ctype)
    REFERENCES CabType(ctype)
);


-- --------------------------------------------------------

CREATE TABLE Place(
    Source varchar(50) NOT NULL,
    Destination varchar(50) NOT NULL,
    distance float NOT NULL,
    PRIMARY KEY(Source, Destination)
);

-- --------------------------------------------------------

CREATE TABLE Travel(
    TravelID varchar(100) NOT NULL,
    DriverID varchar(7) NOT NULL,
    CabID varchar(7) NOT NULL,
    PassengerID varchar(7) NOT NULL,
    Source varchar(50) DEFAULT NULL,
    Destination varchar(50) DEFAULT NULL,
    WaitingPlace varchar(50) DEFAULT NULL,
    Price float DEFAULT NULL,
    WaitingTime varchar(30) DEFAULT NULL,
    StartTime varchar(30) DEFAULT NULL,
    EndTime varchar(30) DEFAULT NULL,
    Rating int DEFAULT NULL,
    PRIMARY KEY(TravelID),
    CONSTRAINT fk_PassengerID_travel
    FOREIGN KEY(PassengerID)
    REFERENCES Passenger(PassengerID),
    CONSTRAINT fk_CabID_travel
    FOREIGN KEY(CabID)
    REFERENCES Cab(CabID),
    CONSTRAINT fk_DriverID_travel
    FOREIGN KEY(DriverID)
    REFERENCES Driver(DriverID)
);

-- --------------------------------------------------------

END TRANSACTION;
