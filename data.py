from csv_reader import load_airports, load_flights
from pyproj import Geod
from merge import resolve_flights


def build_dataset_2020():
    airports = load_airports("airports.csv")
    flights = load_flights("otselennud20.csv")

    routes = resolve_flights(flights, airports)
    lines = []
    for a, b in routes:
        lons, lats = interpolate(a.lon, b.lon, a.lat, b.lat, 300)
        lines.append((lons,lats))
         
    return lines


def build_dataset_2026():
    airports = load_airports("airports.csv")
    flights = load_flights("otselennud26.csv")

    routes = resolve_flights(flights, airports)
    lines = []
    for a, b in routes:
        lons, lats = interpolate(a.lon, b.lon, a.lat, b.lat, 300)
        lines.append((lons,lats))
         
    return lines

def interpolate(lon1, lon2, lat1, lat2, npts):
        geod = Geod(ellps="WGS84")

        points = geod.npts(lon1,lat1,lon2,lat2,npts)

        lons = [lon1] + [p[0] for p in points] + [lon2]
        lats = [lat1] + [p[1] for p in points] + [lat2]

        return lons, lats

