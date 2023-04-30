from flask import Flask, redirect, render_template, request, url_for
from rideon import RideOn as ro

app = Flask(__name__)
curr = ro.Final()

@app.route("/", methods = ["GET"])
def HomePage():
    return render_template("HomePage.html")

@app.route("/AdminLogin.html", methods = ["GET", "POST"])
def AdminLogin():
    if request.method=="POST":
        ausers = curr.get_admin_users()
        usern = request.form["emailinput"]
        pw = request.form["passwordinput"]
        print(ausers, (usern, pw))
        if (usern, pw) in ausers:
            return render_template("HomePageAdmin.html")
        else:
            return render_template("LoginFailed.html")
    return render_template("AdminLogin.html")

@app.route("/PassengerLogin.html", methods = ["GET", "POST"])
def PassengerLogin():
    if request.method=="POST":
        cusers = curr.get_customer_users()
        usern = request.form["emailinput"]
        pw = request.form["passwordinput"]
        print(cusers, (usern, pw))
        if (usern, pw) in cusers:
            return redirect(url_for("HomePagePassenger"))
        else:
            return render_template("LoginFailed.html")
    return render_template("PassengerLogin.html")

@app.route("/DriverLogin.html", methods = ["GET", "POST"])
def DriverLogin():
    if request.method=="POST":
        dusers = curr.get_driver_users()
        usern = request.form["emailinput"]
        pw = request.form["passwordinput"]
        print(dusers, (usern, pw))
        if (usern, pw) in dusers:
            return render_template("HomePageDriver.html")
        else:
            return render_template("LoginFailed.html")
    return render_template("DriverLogin.html")

@app.route("/LoginFailed.html")
def LoginFailed():
    return render_template("LoginFailed.html")

@app.route("/HomePageAdmin.html", methods = ["GET", "POST"])
def HomePageAdmin():
    if request.method=="POST":
        if "first" in request.form:
            return table_template(curr.query_1())
        elif "second" in request.form:
            return table_template(curr.query_2())
        elif "third" in request.form:
            return table_template(curr.query_11())
        elif "fourth" in request.form:
            return table_template(curr.query_12())
        elif "fifth" in request.form:
            return table_template(curr.query_5())
        elif "sixth" in request.form:
            return table_template(curr.query_4())
        elif "seventh" in request.form:
            return table_template(curr.query_3())
    return render_template("HomePageAdmin.html")

@app.route("/HomePagePassenger.html", methods = ["GET", "POST"])
def HomePagePassenger():
    if request.method=="POST":
        ridetype = request.form["ride"]
        cartype = request.form["cartype"]
        pickup = request.form["pickup"]
        drop = request.form["drop"]
        when = request.form["when"]
        curr.insert_searchcabs(ridetype, pickup, drop, cartype)
        drivs = curr.nearby_drivers(ridetype, pickup, cartype)
        d_id = drivs[0][0]
        deets = curr.get_dr_details(d_id)
        curr.insert_booking(d_id, when, pickup, drop, ridetype)
        books = curr.get_booking()
        b_id = books[-1][0]
        curr.insert_trip(b_id, pickup, drop)
        trip = curr.get_trip()
        return booking(drivs, deets, [books[-1]], [trip[-1]])

    return render_template("HomePagePassenger.html")


@app.route("/UpdateLocation.html", methods = ["GET", "POST"])
def UpdateLocation():
    if request.method == "POST":
        street = request.form["streetinput"]
        locality = request.form["localityinput"]
        city = request.form["cityinput"]
        state = request.form["stateinput"]
        pincode = request.form["pincodeinput"]
        curr.insert_location(street, locality, city, state, pincode)
        curr.insert_savedplaces()
    return render_template("UpdateLocation.html")

@app.route("/HomePageDriver.html", methods = ["GET", "POST"])
def HomePageDriver():
    if request.method == "POST":
        if "first" in request.form:
            curr_ride = curr.get_current_ride()
            curr_ride = [curr_ride[-1]]
            return table_template(curr_ride)
        elif "second" in request.form:
            past_books = curr.get_past_bookings()
            return table_template(past_books)
        elif "third" in request.form:
            past_trips = curr.get_past_trips()
            return table_template(past_trips)
    return render_template("HomePageDriver.html")

@app.route("/DriverCab.html", methods = ["GET", "POST"])
def DriverCab():
    vehics = curr.your_vehicles()
    return render_template("DriverCab.html", row1 = vehics)

@app.route("/DriverProfile.html", methods = ["GET", "POST"])
def DriverProfile():
    prof = curr.your_profile()
    return render_template("DriverProfile.html", row1 = prof)


@app.route("/AllRide.html")
def AllRide(query):
    return render_template("AllRide.html", rows = query)

@app.route("/DriverEarning.html")
def DriverEarning():
    q1, q2 = curr.get_wallet()
    return render_template("DriverEarning.html", row1 = q1, row2 = q2)

@app.route("/PastRides.html")
def PastRides():
    q1, q2, q3, q4 = curr.get_rides()
    return render_template("PastRides.html", row1 = q1, row2 = q2, row3 = q3, row4 = q4)

@app.route("/MostVisited.html")
def MostVisited():
    q1 = curr.get_saved_locations()
    return render_template("MostVisited.html", row1 = q1)

if __name__ == "__main__":
    app.run(host="localhost", port=5042, debug = True)