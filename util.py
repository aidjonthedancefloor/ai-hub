import json
import os

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


def assert_openapi_key_set():
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY not set in environment")