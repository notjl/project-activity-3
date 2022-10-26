import requests
from contextlib import suppress

EXTERNAL_V4_API = "https://ident.me/"
EXTERNAL_V6_API = "https://v6.ident.me"

resp = requests.get(EXTERNAL_V4_API)
external_v4 = resp.content.decode("utf8") #To remove binary string

# Try the v6 API endpoint
with suppress(Exception):
    resp_v6 = requests.get(EXTERNAL_V6_API)
    external_v6 = resp.content.decode("utf8")

GEOLOCATION_API = f"https://ipapi.co/{external_v4}/json" #Getting the API Response

resp = requests.get(GEOLOCATION_API)
geolocation_deets = resp.json() #Converting into .json file 

#Printing API Response
print("=" * 50)
print(f"External IPv4 Address:\t\t{geolocation_deets['ip']}")

# Print the IPv6 Address if it is available
with suppress(Exception):
    print(f"External IPv6 Address:\t\t{external_v6}")

print(f"Internet Service Provide:\t{geolocation_deets['org']}")
print(f"Autonomous System Number:\t{geolocation_deets['asn']}")
print(f"Country Code:\t\t\t{geolocation_deets['country_code']}")
print(f"Latitude / Longitude:\t\t{geolocation_deets['latitude']}, {geolocation_deets['longitude']}")
print("=" * 50)
