import csv
from models import Airport
from models import Flight

def load_airports(path: str) -> dict[str, Airport]:
    airports = {}

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            airport = Airport(
                code=row["IATA"],
                lat=float(row["Latitude"]),
                lon=float(row["Longitude"]),
                name=row.get("Name"),
                city=row.get("City"),
            )
            airports[airport.code] = airport

    return airports


def load_flights(path: str) -> list[FlightDest]:
    flights = []

    with open(path, newline="") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            flights.append(
                Flight(
                    origin="TLL",
                    destination=row["IATA"]
                )
            )

    return flights
