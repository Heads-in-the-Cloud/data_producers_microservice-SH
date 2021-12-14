import csv
import requests


def main():
    with open('../data/csv_airplane_types-boeing.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                r = requests.post(
                    f'http://localhost:5000/api/airplane_type/create',
                    json={
                        "type_id": row[0],
                        "max_capacity": row[1]
                    })

                print(str(r.status_code) + " : \n" + r.text)


if __name__ == "__main__":
    main()
