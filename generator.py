import random
import json
import re
import os

import exrex

while True:
    icao = input("Please enter airline ICAO: ").upper()

    # Check if valid ICAO style
    if re.match("^[A-Z]{3}$", icao) is None:
        print(f'"{icao}" is not a valid ICAO code!')
    
    # Check if airline supported
    elif not os.path.exists("airlines/"+icao+".json"):
        print(f'"{icao}" is currently not supported!')

    # Found valid ICAO that is supported
    else:
        break


f = open("airlines/"+icao+".json")
airline = json.load(f)
f.close()

print(f"Generating Callsign for {airline['name']}:")

callsign_regex = random.choice(airline["Conventions"])
callsign = exrex.getone(callsign_regex)

print(airline["ICAO"]+callsign)
