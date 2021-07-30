# CLIMATE CHANGE
#### Video Demo:  <URL HERE>
#### A website that shows you how temperatures have changed in your area.

## LANGUAGES AND LIBRARIES

#### Back-end:

* Python
* Flask
* xarray
* json
* requests

#### Front-end:

* HTML
* CSS
* Javascript

#### API and other data formats:

* Google maps reverse geocoding
* Google maps Javascript API
* IP-API for geolocation
* Word bank global Co2 emissions JSON
* Berkeley Earth Temperature deviation NetCDF

## Back-end inner workings:

This was by far the most interesting part of the project for me to work out, on first instance the back-end collects the user's IP address and sends a request to [ip-api.com](https://ip-api.com/) to identify (roughly) the user location. A more accurate service could've been used to get a more precise location but I elected not to do that as such methods require the user to allow access and can be considered more intrusive in terms of privacy.
The program is able to identify a country and the coordinates the user is connecting from (again, roughly...) and uses these as arguments to interrogate a NetCDF file to calculate the temparature deviation in the area (more on this later) and by consulting a separate JSON file it also works out the amount of Co2 equivalent emissions the user's country has been responsible for in both 1990 and 2018 (the last year that the current database I'm referencing to has the most available data for the most countries).

These are then handed over to the HTML file that displays them.


