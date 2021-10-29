# This script needs to generate and upload (either through the ticket API or each individual
# API) data for:
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

def main(api_path):
    return api_path


if __name__ == "__main__":
    main("http://localhost:5000/api/booking/create")
