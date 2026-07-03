#dict -
dict = {
    "trip_id": 12,
    "pickup": "chennai central",
    "drop": "airport",
    "driver": "boss",
    "status": "completed"

}

print(dict["pickup"])
print(dict.get("driver"))
print(dict.keys())
print(dict.values())
print(dict.update({"age": 27}))
print(dict.pop("age"))
print(dict)