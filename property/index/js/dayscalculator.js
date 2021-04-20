function Days() {
var d1 = document.getElementByName("from_date").value;
alert(d1);
var d2 = document.getElementByName("to_date").value;

var days = parseInt((d2-d1)/(24 * 3600 * 1000));
alert(days);
document.getElementByName("days").value = days;
}

 


