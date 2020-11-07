// This script uses onemap API to convert coordinates between latitude, longitude and SVY21 map grid reference.
// Refer to documentation at https://developers.onemap.sg
// Script requires HTML front page with elements: 'lat, 'long', 'result', 'x_value', 'y_value' & 'result2'

function latlong() {
    lat = document.getElementById("lat").value;
    long = document.getElementById("long").value;
    if (lat !== '' && long !== ''){
      fetch("https://developers.onemap.sg/commonapi/convert/4326to3414?latitude="+lat+"&longitude="+long)
        .then((response) => response.json())
        .then((data) => {
            var mgr_data = data;
            console.log(data);
            if (data.error == 'Please input a latitude and longitude coordinates'){
              document.getElementById('result').innerHTML = "Enter a latitude and longitude";
            } else {
            document.getElementById('result').innerHTML = '';
            var mgr = mgr_data;
            document.getElementById('result').innerHTML = mgr.X + ", " + mgr.Y;
            }
            });
        
    } else {
      document.getElementById('result').innerHTML = "Enter a latitude and longitude";
      }
}


function svy21() {
    x_value = document.getElementById("x_value").value;
    y_value = document.getElementById("y_value").value;
    if (x_value !== '' && y_value !== ''){
      fetch("https://developers.onemap.sg/commonapi/convert/3414to4326?X="+x_value+"&Y="+y_value)
        .then((response) => response.json())
        .then((d) => {
            var latlong_data = d;
            console.log(latlong_data);
            if (latlong_data.code == 'InternalError'){
              document.getElementById('result2').innerHTML = "Enter X (Easting) and Y (Northing) coordinates";
            } else if (latlong_data.error == "Please input a valid X and Y coordinates."){
              document.getElementById('result2').innerHTML = "Enter X (Easting) and Y (Northing) coordinates";
            } else if (latlong_data.error !== "Please input a valid X and Y coordinates.") {
            document.getElementById('result2').innerHTML = '';
            var latlong = latlong_data;
            document.getElementById('result2').innerHTML = latlong.latitude + ", " + latlong.longitude;
            }
            });
        
    } else {
      document.getElementById('result2').innerHTML = "Enter X (Easting) and Y (Northing) coordinates";
      }
}

