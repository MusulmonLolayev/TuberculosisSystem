from . import patient
from .models import Country
from tuberculosis.app import db
from flask import jsonify, request

from .models import Country
from .serializer import CountrySchema

def general_request(request, InstanceCLass, SchemaClass):
    if request.method == "GET":
        instances = InstanceCLass.query.order_by(InstanceCLass.name).all()
        instance_schemas = SchemaClass(many=True)

        return jsonify(instance_schemas.dump(instances)), 200
    print("ss=", request.data)
    return "Error", 400

@patient.route('/country_request', methods= ["GET", "POST", "PUT", "DELETE"])
def country_request():
    return general_request(request, Country, CountrySchema)