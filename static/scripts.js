// require('dotenv').config();

function put_coord(oggietto) {
    const latInput = document.querySelector('#lat');
    const lonInput = document.querySelector('#lon');
    latInput.value = Math.round(oggietto.lat);
    lonInput.value = Math.round(oggietto.lng);
}

// code adapted from https://developers.google.com/maps/documentation/javascript/examples/event-click-latlng#maps_event_click_latlng-javascript
function initMap() {
    const myLatlng = { lat: lat_in , lng: lon_in };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: myLatlng,
    });
    // Create the initial InfoWindow.
    let infoWindow = new google.maps.InfoWindow({
      content: "Click the map to find different Lat/Lng!",
      position: myLatlng,
    });
    infoWindow.open(map);
    // Configure the click listener.
    map.addListener("click", (mapsMouseEvent) => {
      // Close the current InfoWindow.
      infoWindow.close();
      // Create a new InfoWindow.
      infoWindow = new google.maps.InfoWindow({
        position: mapsMouseEvent.latLng,
      });
      const coord = mapsMouseEvent.latLng.toJSON();
      infoWindow.setContent(
        JSON.stringify(coord, null, 2)
      );
      infoWindow.open(map);
      put_coord(coord);
    });
}

