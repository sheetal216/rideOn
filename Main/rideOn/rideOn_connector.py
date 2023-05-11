import psycopg2
import datetime

class Finall():
    def __init__(self) -> None:
        self.db = psycopg2.connect(
            host = "10.17.50.91",
            user = "group_33",
            password = "BuHnPs9GsqNgsUfQ",
            database = "group_33",
            port = 5432
        )
        self.cursor = self.get_cursor()

    def get_cursor(self):
        return self.db.cursor()
    # Getting ridedetail of passenger from travel table 
    def RideDetail(self, passengerId):
        curr = self.db.cursor()
        arr = []
        curr.execute("""CREATE VIEW PassengerTravel AS SELECT TravelID, Source, Destination, WaitingPlace, Price, StartTime, EndTime FROM Travel WHERE Travel.PassengerID = passengerId;""")
        curr.execute("""SELECT * FROM PassengerTravel;""")
        arr = cur.fetchall()
        curr.execute("""DROP VIEW PassengerTravel;""")
        return (list(set(arr)))

    # Getting total earning of driver
    def TotalDriverEarning(self, DriverId):
        curr = self.db.cursor()
        arr = []
        curr.execute("""CREATE VIEW Earn AS SELECT SUM(Travel.price) AS Total_Earning FROM Travel,Driver WHERE Travel.DriverID = DriverId;""")
        curr.execute("""SELECT * FROM Earn;""")
        arr = cur.fetchall()
        curr.execute("""DROP VIEW Earn;""")
        return (list(set(arr)))

    # Finding distance between start and end point check if there is also waiting place
    def FindDistance(self,source, destination,waitingplace):
        curr = self.db.cursor()
        curr.execute("""CREATE VIEW Dist AS WITH Current AS( SELECT * FROM Place) SELECT CASE WHEN waitingplace = NULL AND Place.Source = source AND Place.Destination = destination THEN Place.distance WHEN waitingplace != NULL AND Place.Source = source AND Place.Destination = waitingplace AND Current.Source = waitingplace AND Current.Destination = destination THEN Current.distance + Place.distance ELSE NULL  END AS Distance FROM Current,Place;""" )
        curr.execute("""SELECT * FROM Dist;""")
        arr = []
        arr = curr.fetchall()
        curr.execute("""DROP VIEW Dist;""")
        return (list(set(arr)))
            

    # Updating travel table i.e. inserting new ride
    def NewRide(self, d,travelid,driverid,cabid,passengerid,source, destination, waitingplace,waitingtime,starttime,endtime,rating):
        curr = self.db.cursor()
        curr.execute(
            """INSERT into Travel (TravelID,DriverID, CabID, PassengerID,Source,Destination,WaitingPlace,Price,WaitingTime,StartTime,EndTime ,Rating) values (%s,%s,%s,%s,%s,%s,%s,%f,%s,%s,%s,%i) ;""",
            (travelid,driverid,cabid,passengerid,source,destination,waitingplace,waitingtime,starttime,endtime,rating)
        )
        self.db.commit()
    
    # Getting admin details   
    # admin_users table grant m update krna h
    def AdminDetail(self):
        curr = self.db.cursor()
        curr.execute(
            """CREATE VIEW AdminUser AS SELECT * FROM Passenger;"""
        )
        curr.execute(
            """SELECT * FROM AdminUser;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW AdminUser;"""
        )
        return list(set(temp))

    # Getting Passenger userid and password
    def PassengerDetail(self):
        curr = self.db.cursor()
        curr.execute(
            """CREATE VIEW PassengerUser AS SELECT Passenger.EmailID, Passenger.DateOfBirth FROM Passenger;"""
        )
        curr.execute(
            """SELECT * FROM PassengerUser;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW PassengerUser;"""
        )
        return list(set(temp))


    def DriverDetail(self):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW DriverUser AS SELECT Driver.EmailID, Driver.DateOfBirth FROM Driver; """
        )
        curr.execute(
            """ SELECT * FROM DriverUser; """
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW DriverUser;"""
        )
        return list(set(temp))


    # Getting Top 15 Driver with highest rating
    def findTopDriver_HighRate(self):
        curr = self.db.cursor()
        curr.execute(
            """" CREATE VIEW HighRate As SELECT * FROM Driver ORDER BY Driver.Rating DESC LIMIT 15; """
        )
        curr.execute(
            """SELECT * FROM HighRate;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW HighRate;"""
        )
        return list(set(temp))
    
    # Getting top 15 driver with lowest earning
    def findTopDriver_LowEarn(self):
        curr = self.db.cursor()
        curr.execute(
            """" CREATE VIEW LowEarn As SELECT Driver.* , SUM(Travel.Price) AS Earning FROM DriverID JOIN Driver ON Travel.DriverID = Driver.DriverID GROUP BY Travel.DriverID ORDER BY Earning DESC LIMIT 15; """
        )
        curr.execute(
            """SELECT * FROM LowEarn;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW LowEarn;"""
        )
        return list(set(temp))

    # GETTING TOP 15 Start Location with maximum rides
    def MostVisitedSource(self):
        curr = self.db.cursor()
        curr.execute(
            """" CREATE VIEW TopSource As SELECT Travel.Source, COUNT(Travel.Source) AS TotalRides FROM Travel GROUP BY Travel.Source ORDER BY TotalRides DESC LIMIT 15; """
        )
        curr.execute(
            """SELECT * FROM TopSource;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW TopSource;"""
        )
        return list(set(temp))

    #  Update Driver Location
    def DriverLocation(self,source,driverid):
        curr = self.db.cursor()
        try: 
            curr.execute(
                """ UPDATE Driver SET Driver.Location = source WHERE Driver.DriverID = driverid; """
            )
            self.db.commit()
        except:
            self.db.rollback()
            # IF NOT FINDING ANY Driver with driverid

    # Finding top 15 driver with location equals passenger location
    def FindDriver(self,source,numPassenger):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW AvailDriver AS  
                SELECT Cab.CabID,Cab.ctype, Driver.DriverID, Driver.FirstName, Driver.LastName FROM Driver, Cab, CabType WHERE numPassenger >= Cabtype.MaxPassenger AND Cab.ctype = CabType.ctype AND Driver.DriverID = Cab.DriverID AND Cab.Condition = "Available" ORDER BY Driver.Rating DESC LIMIT 10;"""
        )
        curr.execute(
            """SELECT * FROM AvailDriver;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW AvailDriver;"""
        )
        return list(set(temp))


    def UpdateStatusDriver(self,cabid):
        curr = self.db.cursor()
        try: 
            curr.execute(
                """ UPDATE Cab SET Cab.Condition = "NOT AVAILABLE" WHERE Cab.CabID = cabid; """
            )
            self.db.commit()
        except:
            self.db.rollback()


    def PastBooking(self,driverid):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW pastbook AS SELECT * FROM Travel WHERE Travel.DriverID = driverid; """
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW pastbook;"""
        )
        return list(set(temp))

    def GetPassengerID(self,id,password):
        curr = self.db.cursor()
        curr.execute(
            """CREATE VIEW PassengerUser AS SELECT Passenger.PassengerID FROM Passenger WHERE Passenger.EmailID = id AND Passenger.DateOfBirth = password;"""
        )
        curr.execute(
            """SELECT * FROM PassengerUser;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW PassengerUser;"""
        )
        return list(set(temp))


    # Getting Driver Rating from travel table
    def DriverRating(self,driverid):
        curr = self.db.cursor()
        curr.execute(
            """CREATE VIEW DriverRating AS SELECT AVG(Travel.Rating) FROM Travel WHERE Travel.DriverID = driverid; """
        )
        curr.execute(
            """SELECT * FROM DriverRating;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW DriverRating;"""
        )
        return list(set(temp))

    # Updating Driver Rating
    def UpdateDriverRate(self,driverid,rate):
        curr = self.db.cursor()
        try: 
            curr.execute(
                """ UPDATE Driver SET Driver.Rating = rate WHERE Driver.DriverID = driverid; """
            )
            self.db.commit()
        except:
            self.db.rollback()
        
    # Add new passenger 
    def AddPassenger(self,firstname,lastname,contactnumber,gender,emailid,dob):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW NumPasseneger AS SELECT COUNT(*) FROM Passenger;"""
        )
        curr.execute(
            """ SELECT * FROM NumPasseneger; """ 
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW NumPasseneger;"""
        )
        flag = list(set(temp))
        num = flag[0] + 1
        passengerid = "p" + str(num)
        curr.execute(
            """ INSERT INTO Passenger (PassengerID,FirstName,LastName,ContactNumber,Gender,EmailID,DateOfBirth) values (%s,%s,%s,%s,%s,%s,%s); """,
            (passengerid,firstname,lastname,contactnumber,gender,emailid,dob)
        )
        self.db.commit()

    #Add new driver
    def AddDriver(self,firstname,lastname,contactnumber,gender,emailid,dob):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW NumDriver AS SELECT COUNT(*) FROM Driver;"""
        )
        curr.execute(
            """ SELECT * FROM NumDriver; """ 
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW NumDriver;"""
        )
        flag = list(set(temp))
        num = flag[0] + 1
        driverid = "d" + str(num)
        cabid = "c" + str(num)
        curr.execute(
            """ INSERT INTO Driver (DriverID,FirstName,LastName,ContactNumber,Gender,EmailID,DateOfBirth,Location) values (%s,%s,%s,%s,%s,%s,%s,%s); """,
            (driverid,firstname,lastname,contactnumber,gender,emailid,dob,location)
        )
        self.db.commit()
        return (driverid,cabid)

    #Add Cab
    def AddCab(self,driverid,cabid,cType):
        curr = self.db.cursor()
        curr.execute(
            """ INSERT INTO Cab (DriverID,CabID,ctype,Condition) values (%s,%s,%s,%s); """,
            (driverid,cabid,cType,"Available")
        )
        self.db.commit()
    

    # Passenger Visited location as saved location
    def VisitedLocation(self,passengerid):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW Visit AS SELECT Travel.Destination FROM Travel WHERE Travel.PassengerID = passengerid GROUP BY Travel.PassengerID,Travel.Destination; """
        )
        curr.execute(
            """ SELECT * FROM Visit """
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW Visit;"""
        )
        return list(set(temp))

    #  Getting DriverID by userid AND Password
    def GetDriverID(self,userid,password):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW Driverid AS SELECT Driver.DriverID FROM Driver WHERE Driver.EmailID = userid AND Driver.DataOfBirth = password; """
        )
        curr.execute(
            """ SELECT * FROM Driverid """
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW Driverid;"""
        )
        flag = list(set(temp))
        return flag[0]

    # Check Availability of Driver
    def CheckDriver(self,driverid):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW check As SELECT Cab.Condition FROM Cab WHERE Cab.DriverID = driverid;"""
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW Driverid;"""
        )
        flag = list(set(temp))
        return flag[0]

    #  Getting Driver is available or not by giving its current ride
    def GetPresentRide(self,driverid):
        curr = self.db.cursor()
        curr.execute(
            """ CREATE VIEW Present AS SELECT * FROM Travel WHERE Travel.DriverID = driverid; """
        )
        temp = curr.fetchall()
        curr.execute(
            """DROP VIEW Present;"""
        )
        flag = list(set(temp))
        return flag