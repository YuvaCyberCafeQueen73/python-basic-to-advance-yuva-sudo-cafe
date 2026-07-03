#set - unique
#set - Unordered
#set - syntax - {}

city1 = {"MAA", "BOM", "HKG"}
city2 = {"KUL", "LON", "BOM"}

print("union:", city1.union(city2))

print("interceptor", city1.intersection(city2))

print("difference", city1.difference(city2))

city1.add("ADL")
city1.remove("HKG")
print("add/remove option:", city1)