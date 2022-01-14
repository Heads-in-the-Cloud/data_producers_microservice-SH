# ######################################################################################################################
# ########################################                               ###############################################
# ########################################      Flask Initialization     ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
import requests

from config import Config
from networking import *
import os

from loaders.loader_airplane_type import main as airplane_type_l
from loaders.loader_airport import main as airport_l
from loaders.loader_route import main as route_l
from loaders.loader_user_role import main as user_role_l

from producers.producer_airplanes import main as airplane_p
from producers.producer_users import main as user_p
from producers.producer_flights import main as flight_p
from producers.producer_bookings import main as booking_p

from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
app.config.from_object(Config)


# check to see if the database has already been loaded with the base information
# i.e. GET /api/user_role/1 --> r.status_code == 200  means that the info has been found
# maybe check that user_role 1 is "user" and if info is garbled do a database reset of these tables
def request_check():
    resp = requests.get(f"{USERS_API}/user_role/1")
    if resp.status_code == 400 or resp.status_code == 404:
        return True
    return False


if False:
    airplane_type_l()
    airport_l()
    route_l()
    user_role_l()


@app.route('/')
@app.route('/index')
def proof_of_life():
    return "<p> Data Production microservice, reporting for duty. <p>"


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
    app.run(debug=True, host="0.0.0.0")
