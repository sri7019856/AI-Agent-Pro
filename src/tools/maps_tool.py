import requests

HEADERS = {"User-Agent": "AI-Agent-Pro"}


def geocode(place: str):
    """
    Convert a place name into latitude and longitude.
    """

    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={
            "q": place,
            "format": "json",
            "limit": 1,
        },
        headers=HEADERS,
    )

    data = response.json()

    if not data:
        return None

    return (
        float(data[0]["lat"]),
        float(data[0]["lon"]),
    )


def get_route(origin: str, destination: str):
    """
    Get route information.
    """

    start = geocode(origin)
    end = geocode(destination)

    if start is None:
        return "Origin not found."

    if end is None:
        return "Destination not found."

    start_lat, start_lon = start
    end_lat, end_lon = end

    response = requests.get(
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{start_lon},{start_lat};"
        f"{end_lon},{end_lat}",
        params={
            "overview": "full",
            "geometries": "geojson",
        },
    )

    data = response.json()

    if data["code"] != "Ok":
        return "Unable to calculate route."

    route = data["routes"][0]

    return {
        "distance": route["distance"] / 1000,
        "duration": route["duration"] / 60,
        "geometry": route["geometry"]["coordinates"],
        "start": start,
        "end": end,
        "origin": origin,
        "destination": destination,
    }
