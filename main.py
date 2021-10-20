from user_data_producer import main as user_dp


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


def runner(*args, times=10):

    if "users" or "user" or "u" in [x.lower for x in args]:
        for time in range(0, times):
            user_dp('http://localhost:5000/api/user/create')

    if "flights" or "flight" or "f" in [x.lower for x in args]:
        for time in range(0, times):
            user_dp('http://localhost:5000/api/user/create')

    if "bookings" or "booking" or "b" in [x.lower for x in args]:
        for time in range(0, times):
            user_dp('http://localhost:5000/api/user/create')


if __name__ == "__main__":
    runner("users")
