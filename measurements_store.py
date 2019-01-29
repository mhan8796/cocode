from .measurement import Measurement
from werkzeug.exceptions import abort

### ADDED ###
import sys
import pickle
### ADDED ###

def add_measurement(measurement):
    # TODO:
    #abort(501)
    
    ### ADDED ###
    save_object(measurement,'mydata')
    ### ADDED ###


def get_measurement(date):
    # TODO:
    #abort(501)
    
    ### ADDED ###
    for measurement in pickled_items('mydata'):
        if measurement.timestamp == date:
            return measurement
    return None
    ### ADDED ###


def query_measurements(start_date, end_date):
    # TODO:
    #abort(501)
    
    ### ADDED ###
    ret = []
    for measurement in pickled_items('mydata'):
        if start_date <= measurement.timestamp and measurement.timestamp <= end_date:
            ret.append(measurement)
    return ret
    ### ADDED ###

### ADDED ###
def save_object(obj, filename):
    with open(filename, 'a') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
        
def pickled_items(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break
### ADDED ###

