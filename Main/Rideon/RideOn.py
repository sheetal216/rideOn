import psycopg2
import datetime
import os,sys

class Final():
    def __init__(self) -> None:
        self.db = psycopg2.connect(
    host = "10.17.50.91",
    database = "group_33",
    user = "group_33",
    password = "BuHnPs9GsqNgsUfQ",
    port = 5432
)


    def RideDetail(self, passengerId):
        curr = self.db.cursor()
        arr = []
        curr.execute("CREATE VIEW PassengerTravel AS SELECT TravelID, Source, Destination, WaitingPlace, Price, StartTime, EndTime FROM Travel WHERE Travel.PassengerID = passengerId;")
        curr.execute("SELECT * FROM PassengerTravel;")
        arr = cur.fetchall()
        curr.execute("DROP VIEW PassengerTravel;")
        return (list(set(arr)))

    def TotalDriverEarning(self, DriverId):
        curr = self.db.cursor()
        arr = []
        curr.execute("CREATE VIEW Earn AS SELECT SUM(Travel.price) AS Total_Earning FROM Travel,Driver WHERE Travel.DriverID = DriverId;")
        curr.execute("SELECT * FROM Earn;")
        arr = cur.fetchall()
        curr.execute("DROP VIEW Earn;")
        return (list(set(arr)))

    def FindDistance(self,source, destination,waitingplace):
        curr = self.db.cursor()
        curr.execute("CREATE VIEW Dist AS SELECT CASE WHEN Travel.Waiting_place IS NOT NULL THEN 10 * ((SELECT distance FROM Place Where Place.Source == :source AND Place.Destination == :waiting_place) + (SELECT distance FROM Place Where Place.Source == :waiting_place AND Place.Destination == :destination)) ELSE 10 * (SELECT distance From Place WHERE Place.Source = source AND Place.Destination = destination)  END FROM Place;")
        curr.execute("SELECT * FROM Dist;")
        arr = []
        arr = curr.fetchall()
        curr.execute("DROP VIEW Dist;")
        return (list(set(arr)))
            


    def NewRide(self, travelid,driverid,cabid,passengerid,source, destination, waitingplace,waitingtime,starttime,endtime,rating):
        curr = self.db.cursor()
        dist = FindDistance(source,destination,waitingplace)
        d = dist[0]
        curr.execute(
            """INSERT into Travel (TravelID,DriverID, CabID, PassengerID,Source,Destination,WaitingPlace,Price,WaitingTime,StartTime,EndTime ,Rating) values (%s,%s,%s,%s,%s,%s,%s,%f,%s,%s,%s,%i) ;""",
            (travelid,driverid,cabid,passengerid,source,destination,waitingplace,waitingtime,starttime,endtime,rating)
        )
        self.db.commit()
    
        