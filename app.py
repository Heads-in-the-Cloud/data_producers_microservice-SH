# ######################################################################################################################
# ########################################                               ###############################################
# ########################################      Flask Initialization     ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
import os

from loader_airplane_type import main as airplane_type_l
from loader_airport import main as airport_l
from loader_route import main as route_l
from loader_user_role import main as user_role_l

from producer_airplanes import main as airplane_p
from producer_users import main as user_p
from producer_flights import main as flight_p
from producer_bookings import main as booking_p

from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))

# check to see if the database has already been loaded with the base information
# i.e. GET /api/user_role/1 --> r.status_code == 200  means that the info has been found
# maybe check that user_role 1 is "user" and if info is garbled do a database reset of these tables
request_check = False
if request_check:
    airplane_type_l()
    airport_l()
    route_l()
    user_role_l()


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Restful Resources      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

api = Api(app)


class AirplaneProducer(Resource):
    def get(self):
        airplane_p()


class UserProducer(Resource):
    def get(self):
        user_p()


class FlightProducer(Resource):
    def get(self):
        flight_p()


class BookingProducer(Resource):
    def get(self):
        booking_p()


api.add_resource(AirplaneProducer, '/api/airplane_producer')
api.add_resource(UserProducer, '/api/user_producer')
api.add_resource(FlightProducer, '/api/flight_producer')
api.add_resource(BookingProducer, '/api/booking_producer')

# ######################################################################################################################
# ########################################                               ###############################################
# ########################################         Make Runnable         ###############################################
# ########################################                               ###############################################
# ######################################################################################################################


if __name__ == "__main__":
    app.run(debug=True)
