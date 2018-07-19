# Background
The Applied Mathematics Lab was contracted by the Baltimore Humane Society to evaluate donation history to classify donors, visualize donation data, and understand what factors encourage major donations.

# Geocoding
One of our tasks was to convert a .csv file that consisted of over 20,000 addresses into a set of GPS coordinates. This conversion is known as geocoding. Using the Google Maps API, we were able to geocode over 97% of all addresses provided to us.

In this folder, you will find a sample list of addresses (sample.csv) and a Python file that performs the process of geocoding (geocoding.py). The formatting of sample.csv is as follows (by column): 

ID number, Name, Address1, Address2, Address3, Address4, City, State, Zip Code

However you process an address depends on how many fields you need for an address; geocoding.py accounts for as many as four fields for an address.

Packages required: googlemaps (requires a key from the Google Maps API to work), csv
