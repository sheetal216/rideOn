function formSubmitted()
{
    var e = document.getElementById("emailinput").value;
    var p = document.getElementById("passwordinput").value;
    if (e.toLowerCase()=="driver@coldmail.com" && p=="d123")
        window.location.href = "driver_home.html";
    else
        window.alert("Incorrect Email Id or Password");
}