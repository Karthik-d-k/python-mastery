import csv
import tracemalloc
import typing


def memory_usage(f):
    """
    Print memeory usage of a function `f`
    """
    tracemalloc.start()
    _rows = f("../Data/ctabus.csv")
    current, peak = map(lambda x: x / 10**6, tracemalloc.get_traced_memory())
    print(f"Memory Usage of [{f.__name__}]:\n{current = } MB\n{peak = } MB")


def read_rides_as_tuple(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dict(filename):
    """
    Read the bus ride data as a list of dicts
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                "route": route,
                "date": date,
                "daytype": daytype,
                "rides": rides,
            }
            records.append(record)
    return records


class Ride:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename):
    """
    Read the bus ride data as a list of class intances
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Ride(route, date, daytype, rides)
            records.append(record)
    return records


class NamedRide(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


def read_rides_as_named_tuple(filename):
    """
    Read the bus ride data as a list of named tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = NamedRide(route, date, daytype, rides)
            records.append(record)
    return records


class RideSlot:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class_with_slots(filename):
    """
    Read the bus ride data as a list of class intances with slots
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RideSlot(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == "__main__":
    print("-" * 50)
    memory_usage(read_rides_as_tuple)
    print("-" * 50)
    memory_usage(read_rides_as_dict)
    print("-" * 50)
    memory_usage(read_rides_as_class)
    print("-" * 50)
    memory_usage(read_rides_as_named_tuple)
    print("-" * 50)
    memory_usage(read_rides_as_class_with_slots)
    print("-" * 50)
