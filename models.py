from dataclasses import dataclass

@dataclass(frozen=True)
class Airport:
    code: str
    lat: float
    lon: float
    name: str | None = None
    city: str | None = None


@dataclass(frozen=True)
class Flight:
    origin: str
    destination: str
