function formSubmitted()
{
    var e = document.getElementById("emailinput").value;
    var p = document.getElementById("passwordinput").value;
    if (e.toLowerCase()=="admin@coldmail.com" && p=="a123")
        window.location.href = "HomePageAdmin.html";
    else
        window.alert("Incorrect Email Id or Password");
}