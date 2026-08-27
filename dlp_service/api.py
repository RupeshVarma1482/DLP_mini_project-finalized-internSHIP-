from flask import Flask, jsonify, request
from dlp_service.policies.policy_processing import process_policy
import sys

# policy_info = sys.argv[1]

app = Flask(__name__)

@app.route("/")
def base():
    return jsonify({
        "app": "flask",
        "message": "hello der mah ni gar"
    })

@app.route("/get_file_info", methods = ["POST"])
def get_file_info():
    global policy_info
    data = request.get_json()
    print(f"data received from the extension:")
    print(data)
    print(f"its type is:")
    print(type(data))

    # process_policy(policy_info, file_data)

    return jsonify({
        "allowed": True
    })

if __name__ == "__main__":
    # 127.0.0.1:5000 -> default
    # 127.0.0.1:8765 -> content.js listening on
    app.run(host = "127.0.0.1", port = 5000)