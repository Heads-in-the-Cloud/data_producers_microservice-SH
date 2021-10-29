import requests

from loader_airplane_type import main as airplane_type_l
from loader_airport import main as airport_l
from loader_route import main as route_l
from loader_user_role import main as user_role_l

from producer_users import main as user_p
from producer_flights import main as flight_p
from producer_bookings import main as booking_p

from env_var import user_ms_api
from env_var import flight_ms_api
from env_var import booking_ms_api


def welcome_screen():

    output = ""
    output += "*****************************************************************\n"
    output += "*                                                               *\n"
    output += "*       Welcome to the Utopia Airlines Dummy Data Loader        *\n"
    output += "*                                                               *\n"
    output += "*****************************************************************\n\n\n"

    print(output)


def simple_menu():

    output = ""
    output += "*****************************************************************\n"
    output += "*                                                               *\n"
    output += "* Please enter any of the following commands, space-separated:  *\n"
    output += "*  \"users\"    Run the user data producer                        *\n"
    output += "*  \"flights\"  Run the flight data producer                      *\n"
    output += "*  \"bookings\" Run the booking data producer                     *\n"
    output += "*                                                               *\n"
    output += "*****************************************************************\n\n"

    print(output)


def main():

    # check to see if the user roles table has been filled, if not run the loaders
    r = requests.get(url=f"{user_ms_api}/user_role/1")
    if r.status_code == 404:
        user_role_l(f'{user_ms_api}/user_role/create')
        airplane_type_l(f'{flight_ms_api}/airplane_type/create')
        airport_l(f'{flight_ms_api}/airport/create')
        route_l(f'{flight_ms_api}/route/create')

    print("Please enter your choices as a space-separated list. E.g. \"users flights\"")
    print("would run both the users and flights producers.")
    args = input("input:  ").split()
    num = int(input("How many times? :  "))
    for arg in args:
        runner(arg, times=num)


def runner(*args, times=10):

    choices = [str.lower(x) for x in args]

    if "users" in choices or "user" in choices or "u" in choices:
        for time in range(0, times):
            user_p(f'{user_ms_api}/user/create')

    if "flights" in choices or "flight" in choices or "f" in choices:
        for time in range(0, times):
            flight_p(f'{flight_ms_api}/flight/create')

    if "bookings" in choices or "booking" in choices or "b" in choices:
        for time in range(0, times):
            booking_p(f'{booking_ms_api}/booking/create')


if __name__ == "__main__":
    main()
