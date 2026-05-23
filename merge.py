from models import Flight, Airport

def resolve_flights(
    flights: list[Flight],
    airports: dict[str, Airport],
) -> list[tuple[Airport, Airport]]:
    resolved = []

    for f in flights:
        if f.origin not in airports or f.destination not in airports:
            continue

        resolved.append(
            (airports[f.origin], airports[f.destination])
        )

    return resolved
