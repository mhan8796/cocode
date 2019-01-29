from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements
import sys

def get_stats(stats, metrics, from_datetime, to_datetime):
    # TODO:
    #abort(501)
   
    ### ADDED ###
    ret = []
    measurements = query_measurements(from_datetime,to_datetime)
    
    for stat in stats:
        if stat == 'min':
            for metric in metrics:
                entry = {}
                entry['metrics'] = metric
                entry['stats'] = 'min'
                entry['value'] = min([m.metrics.get(metric) for m in measurements])
                ret.append(entry)
        elif stat == 'max':
            for metric in metrics:
                entry = {}
                entry['metrics'] = metric
                entry['stats'] = 'max'
                entry['value'] = max([m.metrics.get(metric) for m in measurements])
                ret.append(entry)
        elif stat == 'average':
            for metric in metrics:
                entry = {}
                data = [float(m.metrics.get(metric)) for m in measurements]
                entry['metrics'] = metric
                entry['stats'] = 'average'
                entry['value'] = sum(data)/len(data)
                ret.append(entry)
    return ret
    ### ADDED ###