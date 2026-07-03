#tuple - immutable meaning like - no changes
#tuple - *** order/ unorder.

trip_summary = ("UBER", "chennai", "Aiport",450.0, "Completed")

#tuple - loop can iterate
#tuple - len(trip_summary)
#tuple - count
print(trip_summary.count("chennai"))
#tuple - index - if value not means it throw the error.
print(trip_summary.index("Aiport"))

#tuple - immutable.
t = trip_summary[1] = 'palani'
#print(t) -> show error TypeError: 'tuple' object does not support item assignment

