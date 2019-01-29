from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort
from weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
)

### ADDED ###
import sys
from .measurement import Measurement
from weathertracker.measurement_store import get_measurement,add_measurement
### ADDED ###

class MeasurementsAPI(MethodView):

    # features/01-measurements/01-add-measurement.feature
    def post(self):
        
        # TODO:
        #abort(501)
        
        ### ADDED ###
        # Get data
        metrics = {}
        timestamp = 0
        for key in request.form.keys():
            if key == 'timestamp':
                timestamp = request.form.get('timestamp')
                # Check timestamp
                if not timestamp: return abort(400)
                try:
                    timestamp = convert_to_datetime(timestamp)
                except DatetimeConversionException:
                    return abort(400)
            else:
                metrics[key] = request.form.get(key)
                # Check values
                if not metrics.get(key): return abort(400)
                try:
                    float(metrics.get(key))
                except ValueError:
                    return abort(400)
        
        # Add measurement
        measurement = Measurement(timestamp,metrics)
        add_measurement(measurement)
        
        # Return success
        resp = jsonify(success=True)
        resp.status_code = 201
        return resp
        ### ADDED ###
       

    # features/01-measurements/02-get-measurement.feature
    def get(self, timestamp):

        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversionException:
            return abort(400)

        # TODO:
        #abort(501)
        
        ### ADDED ###
        measurement = get_measurement(timestamp)
        if not measurement: return abort(404)
        ret = measurement.metrics
        ret['timestamp']=measurement.timestamp
        return jsonify(ret)
        ### ADDED ###
        
