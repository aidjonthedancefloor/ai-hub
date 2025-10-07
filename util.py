import json

def json_entry_to_str(e):
    if isinstance(e, str):
        return e
    else:
        return json.dumps(e)

def json_entry_to_str_list(e):
    if isinstance(e, list):
        return list(map(json_entry_to_str, e))
    else:
        return [json_entry_to_str(e)]