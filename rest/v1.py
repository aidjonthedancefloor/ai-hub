"""/v1/* REST API endpoints."""

from flask import Response, request, jsonify, Blueprint
from util.json_util import obj_to_json_str_list
from completion.ad_hoc import ad_hoc_complete

v1 = Blueprint('v1', __name__, url_prefix='/v1')

@v1.route('/complete', methods=['POST'])
def _complete():
    """
    POST /complete

    input:
    {
        systemPrompts: [<string>, ...],
        userPrompts: [<string>, ...],
    }

    output:
    {
        response: <string>
    }
    """

    payload = None
    if request.is_json:
        try:
            payload = request.get_json()
        except Exception:
            return jsonify({"error": "Invalid JSON body"}), 400

    # TODO possibly validate fields of `payload`

    if payload and isinstance(payload, dict):
        system_prompts = obj_to_json_str_list(payload.get('systemPrompts', []))
        user_prompts = obj_to_json_str_list(payload.get('userPrompts', []))
    else:
        return jsonify({"error": "Invalid JSON body"}), 400

    try:
        response_stream = ad_hoc_complete(system_prompts, user_prompts)
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Processing failed: {e}"}), 500
    
    return Response(response_stream, content_type='text/plain')