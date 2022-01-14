import requests
from jsons import loads
from random import choice

from math import radians, sin, cos, sqrt, atan2

# ------------------------------------------------------------------------------+
#   Haversine routine below credited to:
#   Nathan A. Rooy
#   June, 2016
#
#   https://nathanrooy.github.io/posts/2016-09-07/haversine-with-python/
# ------------------------------------------------------------------------------+


class Haversine:
    """
    use the haversine class to calculate the distance between
    two lon/lat coordinate pairs.
    output distance available in kilometers, meters, miles, and feet.
    example usage: Haversine([lon1,lat1],[lon2,lat2]).feet
    """

    def __init__(self, coord1, coord2):
        lon1, lat1 = coord1
        lon2, lat2 = coord2

        R = 6371000  # radius of Earth in meters
        phi_1 = radians(lat1)
        phi_2 = radians(lat2)

        delta_phi = radians(lat2 - lat1)
        delta_lambda = radians(lon2 - lon1)

        a = sin(delta_phi / 2.0) ** 2 + \
            cos(phi_1) * cos(phi_2) * \
            sin(delta_lambda / 2.0) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        self.meters = R * c  # output distance in meters
        self.km = self.meters / 1000.0  # output distance in kilometers
        self.miles = self.meters * 0.000621371  # output distance in miles
        self.feet = self.miles * 5280  # output distance in feet


class Airport:

    def __init__(self, json):
        self.iata_id = json["iata_id"]
        self.city = json["city"]
        self.name = json["name"]
        self.longitude = json["longitude"]
        self.latitude = json["latitude"]
        self.elevation = json["elevation"]


class Route:

    def __init__(self, origin: Airport, destination: Airport):
        self.origin_id = origin.iata_id
        self.destination_id = destination.iata_id

        # Setting the coordinates
        coordinates1 = [origin.latitude, origin.longitude]
        coordinates2 = [destination.latitude, destination.longitude]
        # Determining the distance via Haversine formula (+-0.8% error margin)
        distance = Haversine(coordinates1, coordinates2).miles
        # average flight speed of most domestic flights in the US in miles per hour
        average_flight_speed = 500

        self.duration = distance / average_flight_speed
        # Note this distance will grossly underestimate actual flight time, since appropriate cruising altitude
        # must be ascended to and descended from.


def main():
    r = requests.get('http://flights:5000/api/v1/airports/')
    airports_json = loads(r.text)

    airports_list = []
    for json in airports_json:
        airport = Airport(json)

        airports_list.append(airport)

    origins = airports_list
    destinations = airports_list

    for origin in origins:
        # pick a random destination from the destinations list
        destination = choice(destinations)

        # if origin and destination are the same, pick again until they aren't
        while origin == destination:
            destination = choice(destinations)

        # create a route from the given airports and send it to the API endpoint
        route = Route(origin, destination)
        r = requests.post(
            'http://flights:5000/api/v1/routes/',
            json={
                "origin_id": route.origin_id,
                "destination_id": route.destination_id,
                "duration": route.duration
            })

        print(str(r.status_code) + " : \n" + r.text)


if __name__ == "__main__":
    main()
