from flask import Flask, redirect, render_template, request, url_for
from rideOn import rideOn_connector as ro

app = Flask(__name__)
curr = ro.Finall()

@app.route('/', methods = ['GET'])
def HomePage():
    return render_template('HomePage.html')

@app.route('/AdminLogin.html', methods = ['GET', 'POST'])
def AdminLogin():
    if request.method=='POST':
        AdminUser = curr.AdminDetail()
        UserId = request.form.get('emailinput')
        PassWord = request.form.get('passwordinput')
        print(AdminUser, (UserId, PassWord))
        if (UserId, PassWord) in AdminUser:
            return redirect(url_for('HomePageAdmin',UserId = UserId, PassWord = Password))
        else:
            redirect(url_for('LoginFailed.html'))
    return render_template('AdminLogin.html')


@app.route('/PassengerLogin.html', methods = ['GET', 'POST'])
def PassengerLogin():
    if request.method=='POST':
        PassengerUser = curr.PassengerDetail()
        UserId = request.form.get('emailinput')
        PassWord = request.form.get('passwordinput')
        print(PassengerUser, (UserId, PassWord))
        if (UserId, PassWord) in PassengerUser:
            pid = curr.GetPassengerID(UserId,PassWord)
            # HomePagePassenger(pid)
            # return redirect(url_for('HomePagePassenger',passengerid = pid))
            return render_template('HomePagePassenger.html')
        else:
            # return redirect(url_for('SignUp'))
            return render_template('SignUp.html')
    return render_template('PassengerLogin.html')




@app.route('/DriverLogin.html', methods = ['GET', 'POST'])
def DriverLogin():
    if request.method=='POST':
        DriverUser = curr.DriverDetail()
        UserId = request.form.get('emailinput')
        PassWord = request.form.get('passwordinput')
        print(dusers, (UserId, PassWord))
        if (UserId, PassWord) in DriverUser:
            driverid = curr.GetDriverID(UserId,PassWord)
            return redirect(url_for('HomePageDriver.html',driverid))
        else:
            return redirect(url_for('SignUp'))
    return render_template('DriverLogin.html')



@app.route('/LoginFailed.html')
def LoginFailed():
    return render_template('LoginFailed.html')



@app.route('/HomePageAdmin.html', methods = ['GET', 'POST'])
def HomePageAdmin():
    if request.method=='POST':
        if 'first' in request.form:
            return table_template(curr.findTopDriver_HighRate())
        elif 'second' in request.form:
            return table_template(curr.findTopDriver_LowEarn())
        elif 'third' in request.form:
            return table_template(curr.MostVisitedSource())
    return render_template('HomePageAdmin.html')


@app.route('/HomePagePassenger.html', methods = ['GET', 'POST'])
def HomePagePassenger(passengerid):
    if request.method=='POST':
        source = request.form.get('Source')
        waitingplace = request.form.get('Waiting Place')
        destination = request.form.get('Destination')
        numPassenger = requqst.form.get('Total Passenger')
        starttime = request.form.get('Start Time')
        waitingtime = request.form.get('Waiting Time')
        distance = curr.FindDistance(source,waitingplace,destination)
        # endtime = starttime + waitingtime + (distance * 10) #Abhi Temporary hai end time
        driver_data = curr.FindDriver(source,numPassenger)
        # curr.NewRide(travelid,driverid,cabid,passengerid,source,destination,waitingplace,waitingtime,starttime,endtime)
        # CabBooking()
        return redirect(url_for('CabBooking',distance = distance,driver_data = driver_data,passengerid = passengerid,source = source,destination = destination,waitingplace = waitingplace,waitingtime = waitingtime,starttime = starttime))
    return render_template('HomePagePassenger.html')



@app.route('/SignUp.html', methods = ['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        firstname = request.form.get('First Name')
        lastname = request.form.get('Last Name')
        contactnumber = request.form.get('Contact Number')
        gender = request.form.get('Gender')
        emailid = request.form.get('Email ID')
        dob = request.form.get('Date of Birth')
        typee = request.form.get('TYPE')
        if typee == 'Passenger':
            curr.AddPassenger(firstname,lastname,contactnumber,gender,emailid,dateofbirth)
            return redirect(url_for('PassengerLogin'))
        else : 
            # DriverSignUp(firstname,lastname,contactnumber,gender,emailid,dateofbirth)
            return redirect(url_for('DriverSignUp',firstname = firstname,lastname = lastname,contactnumber = contactnumber,gender = gender,emailid = emailid,dateofbirth = dateofbirth))
    return render_template('SignUp.html')

@app.route('/DriverSignUp.html', methods = ['GET', 'POST'])     
def DriverSignUp(firstname,lastname,contactnumber,gender,emailid,dateofbirth):
    if request.method == 'POST' :
        location = request.form.get('Location')
        (driverid,cabid) = curr.AddDriver(firstname,lastname,contactnumber,gender,emailid,dateofbirth,location)
        cType = request.form.get('Cab Type')
        curr.AddCab(driverid,cabid,cType)
        return redirect(url_for('DriverLogin'))
    return render_template('DriverSignUp.html')


@app.route('/HomePageDriver.html', methods = ['GET', 'POST'])
def HomePageDriver(driverid):
    if request.method == 'POST':
        PastRide = curr.GetPresentRide(driverid)
        if 'first' in request.form:
            check = curr.CheckDriver(driverid)
            PresentRide = []
            if check == "Available" :
                PresentRide = [curr_r[-1]]
            return table_template(PresentRide)
        elif 'second' in request.form:
            return table_template(PastRide)
    return render_template('HomePageDriver.html')


# CabBooking HO GYA
@app.route('/CabBooking.html')
def CabBooking(distance,driver_data,passengerid,source,destination,waitingplace,waitingtime,starttime):
    if request.method=='POST':
        num = request.form.get('Index')
        currentDriver = driver_data[num-1]
        driverid = currentDriver[2]
        cabid = currentDriver[0]
        travelid = ''.join(random.choice(string.ascii_letters) for i in range(99)) #GEnerating random string for TravelID
        # EndRide(distance,driverid,cabid,travelid,passengerid,source,destination,waitingplace,waitingtime,starttime)
        return redirect(url_for('EndRide',distance = distance,driverid = driverid,cabid = cabid,travelid =travelid,passengerid = passengerid,source = source,destination = destination,waitingplace = waitingplace,waitingtime = waitingtime,starttime = starttime))
    return render_template('CabBooking.html', row1 = drivs, row2 = currentDriver)

# RIDE END HO GYI
@app.route('/EndRide.html')
def EndRide(distance,driverid,cabid,travelid,passengerid,source,destination,waitingplace,waitingtime,starttime):
    if request.method=='POST':
        rate = request.form.get('Rating')
        endtime = request.form.get('End Time')
        curr.NewRide(distance,travelid,driverid,cabid,passengerid,source,destination,waitingplace,waitingtime,starttime,endtime)
        curr.UpdateDriverRate(driverid,rate)
        temp = curr.DriverRating(driverid)
        return redirect(url_for('HomePageDriver',driverid = driverid))
    return render_template('EndRide.html')
        

@app.route('/table_template.html')
def table_template(query):
    return render_template('table_template.html', rows = query)

@app.route('/VisitedLocation.html')
def VisitedLocation(passengerid):
    visit = curr.VisitedLocation(passengerid)
    return render_template('VisitedLocation.html', row1 = visit)


if __name__ == '__main__':
    app.run(host="localhost", port=5432,debug = True)
