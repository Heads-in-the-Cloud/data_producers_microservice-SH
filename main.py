from data_producer_users import main as user_dp
from data_producer_flights import main as flight_dp
from data_producer_bookings import main as booking_dp


def welcome_screen():
    output = ""
    output += "************************************************************\n"
    output += "*                                                          *\n"
    output += "*    Welcome to the Utopia Airlines Dummy Data Loader      *\n"
    output += "*                                                          *\n"
    output += "************************************************************\n"

    print(output)


def simple_menu():
    output = ""
    output += "************************************************************\n"
    output += "*                                                          *\n"
    output += "*  Please enter any of the following commands:               *\n"
    output += "*  \"users\"    Run the user data producer                   *\n"
    output += "*  \"flights\"  Run the flight data producer                 *\n"
    output += "*  \"bookings\" Run the booking data producer                *\n"
    output += "*                                                          *\n"
    output += "*  \"times=<number>\" to specify the number of times to run  *\n"
    output += "*                                                          *\n"
    output += "************************************************************\n"

    print(output)


def main():

    print("Please enter your choices as a space-separated list. E.g. \"users flights\"")
    print("would run both the users and flights producers.")
    args = input("input:  ").split()
    num = int(input("How many times? :  "))
    for arg in args:
        runner(arg, times=num)


def runner(*args, times=2):

    choices = [str.lower(x) for x in args]

    if "users" in choices or "user" in choices or "u" in choices:
        for time in range(0, times):
            user_dp('http://localhost:5000/api/user/create')

    if "flights" in choices or "flight" in choices or "f" in choices:
        for time in range(0, times):
            flight_dp('http://localhost:5000/api/flight/create')

    if "bookings" in choices or "booking" in choices or "b" in choices:
        for time in range(0, times):
            booking_dp('http://localhost:5000/api/booking/create')


if __name__ == "__main__":
    main()
