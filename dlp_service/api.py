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
        file = request.files["fileContent"]
        print(f"file received:", file)
        
        print(f"the type of file is: {type(file)}")
        print(f"the type of file_metadata is: {type(file_metadata)}")

        data = file.read(20)
        print(f"data: {data} | it's type is: {type(data)}", end = "\n\n\n\n\n\n\n")
        # text = data.decode("utf-8")
        # print(f"text: {text}")
        
        return jsonify(process_policy(file_metadata, file))
        
        # return jsonify(decision)

        # return jsonify({
        #     "allowed": True
        # })
    except Exception as e:
        print(f"ERROR:", repr(e))
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000)