
Data Tables

--------------------------------------------------------------------------
--  Driver table

Driver_id	A unique code asssigned to each Driver
First_name	First Name
Last_name​	Last Name
Contact_number​	Contact number
Gender​		Gender
Rating​		Rating earned by driver from customer's
Age		Age

--------------------------------------------------------------------------
--  CabType table
Cab_type	Type of cab 
Price		basic price that it will charge extra other than travel price
Waiting_price	charges that it will take for waiting 
Max_passenger	capacity of cab

--------------------------------------------------------------------------
--  Cab table
Cab_id		Unique Id of the cab
Condition	Status of cab's working condition
Cab_type	Type of cab
Driver_id	Driver ID code

--------------------------------------------------------------------------
--  Travel table
Travel_id​	A unique code asssigned to each journey
Source​		Starting place of travel
Destination​	Destination​ place of travel
Waiting_place​	Place where cab have to wait 
Start_time​	Start time of journey
End_time​	End time of journey
Waiting_time​	Waiting time in journey
Passenger_id​	Passenger ID
Cab_id​		Cab ID
Driver_id	Driver ID

--------------------------------------------------------------------------
--  Passenger table
Passenger_id​	A unique code asssigned to each Passenger
First_name	First Name
Last_name​	Last Name
Contact_number​	Contact number
Gender​		Gender
Email_id	Email ID

--------------------------------------------------------------------------
--  Place table
Place_name	Name of Place
Price		Travel charges in between Destination and Source place

--------------------------------------------------------------------------
--  Review table
Rating_id​	A unique code asssigned to each Rating
Comment​		Comment
Rating​		Rating for journey
Passenger_id​	Passenger ID
Driver_id​	Driver ID
Travel_id	Travel ID
