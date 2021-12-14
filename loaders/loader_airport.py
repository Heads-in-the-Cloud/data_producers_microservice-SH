import csv
import requests


def parser(csv_file, api_path):
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            r = requests.post(
                api_path,
                json={
                    "iata_id": row[0],
                    "city": row[1],
                    "name": row[2],
                    "latitude": row[3],
                    "longitude": row[4],
                    "elevation": row[5]
                })

            print(str(r.status_code) + " : \n" + r.text)


def main(extra=False):
    with open('../data/csv_airports.csv') as csv_file:
        parser(csv_file, 'http://flights:5000/api/airport/create')
    if extra:
        with open('airports_medium.csv') as csv_file:
            parser(csv_file, 'http://flights:5000/api/airport/create')


if __name__ == "__main__":
    main(extra=False)
