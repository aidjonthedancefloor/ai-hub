"""Utility functions for JSON handling."""
import json

def obj_to_json_str(e):
    """Convert an object to a JSON string. If it's already a string, return as is."""
    if isinstance(e, str):
        return e
    else:
        return json.dumps(e)

def obj_to_json_str_list(e):
    """Convert an object or list of objects to a list of JSON strings."""
    if isinstance(e, list):
        return list(map(obj_to_json_str, e))
    else:
        return [obj_to_json_str(e)]
