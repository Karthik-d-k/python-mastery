import read_rides
from collections import Counter

rows = read_rides.read_rides_as_dict("../Data/ctabus.csv")


# 1. How many bus routes exist in Chicago ?
n_routes = len({o["route"] for o in rows})
print(f"Number of bus routes in chicago = {n_routes}")


# 2. How many people rode the number 22 bus on February 2, 2011 ?
n_people_22 = sum([o["rides"] for o in rows if o["date"] == "02/02/2011" and o["route"] == "22"])
print(f"Number of people who rode the number 22 bus on February 2, 2011 = {n_people_22}")
# What about any route on any date of your choosing ?
n_people_12 = sum([o["rides"] for o in rows if o["date"] == "03/10/2011" and o["route"] == "12"])
print(f"Number of people who rode the number 22 bus on March 10, 2011 = {n_people_12}")


# 3. What is the total number of rides taken on each bus route ?
n_rides= Counter()
for r in rows:
    n_rides[r["route"]] += r["rides"]
print(f"Total number of rides taken on each bus route = {n_rides}", sep="\n")


# 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011 ?
n_rides_2001= Counter()
n_rides_2011= Counter()
for r in rows:
    if "2001" in r["date"]:
        n_rides_2001[r["route"]] += r["rides"]
    elif "2011" in r["date"]:
        n_rides_2011[r["route"]] += r["rides"]

n_rides = (n_rides_2011 - n_rides_2001).most_common(5)
print(f"five bus routes which had the greatest ten-year increase in ridership from 2001 to 2011 = {n_rides}", sep="\n")
