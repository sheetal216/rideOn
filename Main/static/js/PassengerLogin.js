function formSubmitted()
{
    var e = document.getElementById("emailinput").value;
    var p = document.getElementById("passwordinput").value;
    if (e.toLowerCase()=="customer@coldmail.com" && p=="c123")
        window.location.href = "HomePagePassenger.html";
    else
        window.alert("Incorrect Email Id or Password");
}