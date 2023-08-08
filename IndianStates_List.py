import json
IndianStates_Cities={"Kerala": "Trivandrum","Tamil Nadu": "Chennai","Goa": "Panaji",
"Gujrat": "GandhiNagar","Hariyana": "Chandigarh","Assam": "Dispur","Karnataka": "Bengaluru"}
print(IndianStates_Cities)
with open("IndianStates_Cities.json","w") as f:
 json.dump(IndianStates_Cities,f)
print("Json completed")
