
from jsonschema import validate

def validate_schema(response_data, schema):
    validate(
        instance=response_data,
        schema=schema
    )