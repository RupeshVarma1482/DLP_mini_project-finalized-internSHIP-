from flask import Flask, jsonify, request
from dlp_service.policies.policy_processing import process_policy
import sys
import json

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
    print(f"route HIT")
    print(f"form keys:", request.form.keys())
    print(f"files keys:", request.files.keys())
    try:
        file_metadata = json.loads(request.form["fileMetadata"])
        print(f"file_metadata received:", file_metadata)
        # file_content = request.files["fileContent"]
        file_content = request.form["fileContent"]
        print(f"file_content received:", file_content)
        
        print(f"the type of file_content is: {type(file_content)}")
        print(f"the type of file_metadata is: {type(file_metadata)}")
        # process_policy(policy_info, file_data)

        return jsonify({
            "allowed": True
        })
    except Exception as e:
        print(f"ERROR:", repr(e))
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    # 127.0.0.1:5000 -> default
    # 127.0.0.1:8765 -> content.js listening on
    app.run(host = "127.0.0.1", port = 5000)