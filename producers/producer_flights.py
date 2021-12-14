import json
import random
from datetime import datetime
import requests

def main():

  # list and select route
  # routes = json.load(requests.get("http://flights:5000/api/route/all"))
  routes = [
    {
      'id': 1,
      'origin_id': 'CLE',
      'destination_id': 'LAX',
      'duration': 6
    },
    {
      'id': 2,
      'origin_id': 'MIA',
      'destination_id': 'LAX',
      'duration': 5
    }
  ]
  # pick a random route from the list
  route = random.choice(routes)

  # list and select airplane
  # airplanes = requests.get('http://flights:5000/api/airplane/all')
  airplanes = [
    {
      'id': 1,
      'type_id': 747
    },
    {
      'id': 2,
      'type_id': 868
    }
  ]

  airplane = random.choice(airplanes)

  # create id num (should be automatic)

  # create departure time
  offset = random.randint(2, 18)
  departure_time = datetime.utcnow

  # start off with no reserved seats
  res_seats = 0

  # create seat price (should be function of route duration)
  seat_price = route['duration'] * 79.83

  flight_data = json.dumps({
    'route_id': route['id'],
    'airplane_id': airplane['id'],
    'departure_time': departure_time,
    'reserved_seats': res_seats,
    'seat_price': seat_price
  })

  try:
    requests.post('http://flights:5000/api/', json=flight_data)
  except:
    print("An error occurred trying to load the data to the end point, please ensure that all services are up.")
    return False

  return True


if __name__ == "__main__":
    main()
