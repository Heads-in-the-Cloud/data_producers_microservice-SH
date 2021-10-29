import random
import requests as requests
from names import get_first_name, get_last_name


def random_dob_creator():
    random.seed()
    year = random.randint(0, 65) + 1955
    month = random.randint(1, 12)
    if month in [1, 3, 5, 7, 8, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 10, 11]:
        day = random.randint(1, 30)
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)

    return f"{month}-{day}-{year}"
    # replace with POST request to user creation API endpoint


def phone_number_creator():
    result = "("

    for i in range(1, 13):
        if i == 4:
            result += ")-"
        elif i == 8:
            result += "-"
        else:
            result += str(random.randint(0, 9))

    return result


def password_generation():
    return "ThisIsABadPasswordBro"


def main(api_path: str):
    role_id = 1                     # This is for creating generic passenger users
    first_name = get_first_name()
    last_name = get_last_name()
    username = f"{first_name}.{last_name}" + str(random.randint(1, 10000))
    password = password_generation()
    dob = random_dob_creator()
    email = f"{first_name}.{last_name}@example.com"
    phone_number = phone_number_creator()

    r = requests.post(
        api_path,
        json={
            "role_id": role_id,
            "given_name": first_name,
            "family_name": last_name,
            "username": username,
            "email": email,
            "password": password,
            "phone": phone_number
        })

    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    main("http://localhost:5000/api/user/create")
