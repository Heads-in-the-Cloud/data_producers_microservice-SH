import requests
from jsons import loads
from random import choice
from haversine import Haversine


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


def main(api_path):
    r = requests.get('http://localhost:5000/api/airport/all')
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
            api_path,
            json={
                "origin_id": route.origin_id,
                "destination_id": route.destination_id,
                "duration": route.duration
            })

        print(r.status_code, r.text)


if __name__ == "__main__":
    main('http://localhost:5000/api/route/create')
