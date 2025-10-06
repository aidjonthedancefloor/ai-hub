from flask import Flask, request, jsonify
from util import json_entry_to_str_list
from complete import complete
import dotenv

app = Flask(__name__)

@app.route('/complete', methods=['POST'])
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
        system_prompts = json_entry_to_str_list(payload.get('systemPrompts', []))
        user_prompts = json_entry_to_str_list(payload.get('userPrompts', []))
    else:
        return jsonify({"error": "Invalid JSON body"}), 400

    try:
        response = complete(system_prompts, user_prompts)
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Processing failed: {e}"}), 500

    return jsonify({"response": response})


if __name__ == '__main__':
    dotenv.load_dotenv()

    # Run on 127.0.0.1:5000 by default
    app.run(host='127.0.0.1', port=5000, debug=True)
