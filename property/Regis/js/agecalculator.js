function ageCount() {
var DOB = document.getElementById("birth_date").value;
var millisecondsBetweenDOBAnd1970 = Date.parse(DOB);
var millisecondsBetweenNowAnd1970 = Date.now();
var ageInMilliseconds = millisecondsBetweenNowAnd1970-millisecondsBetweenDOBAnd1970;
//--We will leverage Date.parse and now method to calculate age in milliseconds refer here https://www.w3schools.com/jsref/jsref_parse.asp

  var milliseconds = ageInMilliseconds;
  var second = 1000;
  var minute = second*60;
  var hour = minute*60;
  var day = hour*24; 
/*using 30 as base as months can have 28, 29, 30 or 31 days depending a month in a year it itself is a different piece of comuptation*/
  var year = day*365;

//let the age conversion begin
var years = Math.round(milliseconds/year);
document.getElementById("age").value = years;
}

 


