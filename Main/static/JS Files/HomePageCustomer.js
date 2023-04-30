var current = '';
var ridetype = "city_ride";

window.onload=function()
{
    current = 'opt1';
    document.getElementById(current).style.backgroundColor = 'rgba(203, 299, 0, 1)';
};

function rideTypeSelected(id)
{
    var choice = document.getElementById(id);
    if (!(id === current))
    {
        document.getElementById(current).style.backgroundColor = 'rgba(0, 0, 0, 0)';
        choice.style.backgroundColor = 'rgba(203, 299, 0, 1)';
        current = id;
        if (id === 'opt1')
            ridetype = "city_ride";
        else if (id === 'opt2')
            ridetype = "shared";
        else if (id === 'opt3')
            ridetype = "rental";
        else
            ridetype = "outstation";
    }
}

function viewMessage()
{
    window.location.href = "messages.html";
}