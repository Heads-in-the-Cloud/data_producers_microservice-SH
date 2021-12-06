# This script needs to generate and upload (either through the ticket API or each individual API) data for:
#       Booking
#           id
#           is_active (always on)
#           confirmation_code (password_generator?)
#       Booking_Payment
#           booking_id (from above)
#           stripe_id (password generator?)
#           refunded (always false)
# Then the booking needs to select randomly between user or guest:
#       Booking_Guest
#           booking_id (from above)
#           contact_email (names package plus formatting)
#           contact_phone (phone_number_generator in user data producer)
#       Booking_User
#           booking_id (from above)
#           user_id (from ticket or look up from API or create new one/call user_d_p)
import requests
from uuid import uuid4
from random import randint
from names import get_first_name, get_last_name
import json


def phone_number_creator():
    result = "("

    for i in range(1, 13):
        if i == 4:
            result += ")-"
        elif i == 8:
            result += "-"
        else:
            result += str(randint(0, 9))

    return result


def email_creator():
    email_providers = [
        "gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com",
        "live.com", "rediffmail.com", "outlook.com", "cox.net"
    ]

    return get_first_name() + "_" + get_last_name() + "@" + email_providers[randint(1, 9)]



def main():

    # Basic data
    booking_data = {
        'id': uuid4(),
        'is_active': True,
        'confirmation_code': uuid4()
    }
    try:
        requests.post('bookings:5000/api/booking/create', json=json.dumps(booking_data))
    except:
        print("An error has occurred trying to upload the basic booking data. Aborting process...")
        return False

    # Payment data
    payment_data = {
        'booking_id': booking_data['id'],
        'stripe_id': "stripe+" + str(uuid4()),
        'refunded': False
    }
    try:
        requests.post('bookings:5000/api/booking_payment/create', json=json.dumps(payment_data))
    except:
        print("An error has occurred trying to upload the booking's payment data. Rolling back and aborting process...")
        requests.get(f"http://bookings:5000/api/booking/delete/{booking_data['id']}")
        return False

    # Guest or User
    path_choice = randint(1, 2)

    if path_choice == 1:
        # Process as guest
        booking_guest = {
            'booking_id': booking_data['id'],
            'contact_email': email_creator(),
            'contact_phone': phone_number_creator()
        }

        try:
            requests.post('users:5000/api/booking_guest/create', json=json.dumps(booking_guest))
        except:
            print(
                "An error has occurred trying to upload the booking's guest data. Rolling back and aborting process...")
            requests.get(f"http://bookings:5000/api/booking/delete/{booking_data['id']}")
            requests.get(f"http://bookings:5000/api/booking_payment/delete/{booking_data['id']}")
            return False
    else:
        # Process as user
        booking_user = {
            'booking_id': booking_data['id'],
            'user_id': 101   # needs to be pulled from the list of available users
        }

        try:
            requests.post('users:5000/api/booking_user/create', json=json.dumps(booking_user))
        except:
            print(
                "An error has occurred trying to upload the booking's guest data. Rolling back and aborting process...")
            requests.get(f"http://bookings:5000/api/booking/delete/{booking_data['id']}")
            requests.get(f"http://bookings:5000/api/booking_payment/delete/{booking_data['id']}")
            return False

    return True


if __name__ == "__main__":
    main()
