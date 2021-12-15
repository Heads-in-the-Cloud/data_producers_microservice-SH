import requests
import csv


def main():
    with open('../data/csv_roles.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                r = requests.post(
                    'http://users:5000/api/user_role/create',
                    json={
                        "role_id": row[0],
                        "name": row[1]
                    })

                print(str(r.status_code) + " : \n" + r.text)


if __name__ == "__main__":
    main()
