from json import loads
from random import choice

import requests

from env_var import flight_ms_api


class AirplaneType:

    def __init__(self, json):
        self.id = json["type_id"]
        self.max_cap = json["max_capacity"]


class Airplane:

    def __init__(self, airplane_id, type_id):
        self.id = airplane_id
        self.type_id = type_id


def main():
    # pulling the list of available airplane types
    r = requests.get(url=f"{flight_ms_api}/airplane_type/all")
    # loading it as a JSON array
    types_json = loads(r.text)
    # pulling out the type ids
    types_list = [json["id"] for json in types_json]

    r = requests.post(
        f"{flight_ms_api}",
        json={
            "type_id": choice(types_list)
        }
    )

    print(str(r.status_code) + " : \n" + r.text)


if __name__ == "__main__":
    main()
