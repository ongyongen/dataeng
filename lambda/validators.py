import jsonschema
from jsonschema import validate
from schema import *

def validate_results_schema(data):
    try:
        for record in data:
            validate(instance=record, schema=results_schema)
            for i in range(len(record)):
                if len(record['restaurants']) != 0:
                    validate(instance=record['restaurants'][i], schema=restaurants_schema)
                    
        print("Data conforms to the schema.")
        
    except jsonschema.exceptions.ValidationError as e:
        print("Data does not conform to the schema.")
        print(e)
        
def validate_events_schema(data):            
    try:
        for record in data:
            if len(record['event']) != 0:
                validate(instance=record["event"], schema=events_schema)
                
        print("Data conforms to the schema.")

    except jsonschema.exceptions.ValidationError as e:
        print("Data does not conform to the schema")
        print(e)