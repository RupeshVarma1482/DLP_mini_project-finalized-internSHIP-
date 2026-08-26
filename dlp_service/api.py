from flask import Flask, jsonify, request
from dlp_service.policies.policy_processsing import process_policy

app = Flask(__name__)

@app.route("/")
def base():
    return jsonify({
        "app": "flask",
        "message": "hello der mah ni gar"
    })

@app.route("/get_file_info", methods = ["POST"])
def get_file_info():
    data = request.get_json()
    print(f"data received from the extension:")
    print(data)
    print(f"its type is:")
    print(type(data))
    policy_criteria = process_policy(data)

    return jsonify({
        "allowed": True
    })

if __name__ == "__main__":
    # 127.0.0.1:5000 -> default
    # 127.0.0.1:8765 -> content.js listening on
    app.run(host = "127.0.0.1", port = 5000)