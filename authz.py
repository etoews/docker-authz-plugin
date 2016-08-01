import base64, json

from flask import Flask, jsonify, request

app = Flask(__name__)
application = app


def _has_said_hello():
    with open('/var/run/authz-said-hello.txt', 'r') as hello_file:
        has_said_hello = hello_file.read()

    return has_said_hello == 'True'

def _set_said_hello(said_hello):
    with open('/var/run/authz-said-hello.txt', 'w') as hello_file:
        hello_file.write(str(said_hello))

@app.route("/")
def index():
    return "Docker Authz Plugin"

@app.route("/Plugin.Activate", methods=['POST'])
def activate():
    return jsonify({'Implements': ['authz']})

@app.route("/AuthZPlugin.AuthZReq", methods=['POST'])
def authz_request():
    print("AuthZ Request")
    print(request.data)

    has_said_hello = _has_said_hello()

    if has_said_hello:
        response = {"Allow": True,
                    "Msg":   "The request authorization succeeded.",
                    "Err":   "The error message if things go wrong."}
    else:
        encoded_request = json.loads(request.data)['RequestBody']
        docker_request = json.loads(base64.b64decode(encoded_request))

        if docker_request['Image'] == 'hello-world':
            _set_said_hello(True)
            response = {"Allow": True,
                        "Msg":   "The request authorization succeeded. Thanks for saying hello!",
                        "Err":   "The error message if things go wrong."}
        else:
            response = {"Allow": False,
                        "Msg":   "The request authorization failed. You must say hello first",
                        "Err":   "You must say hello first."}

    return jsonify(**response)

@app.route("/AuthZPlugin.AuthZRes", methods=['POST'])
def authz_response():
    print("AuthZ Response")
    response = {"Allow": True,
                "Msg":   "The response authorization succeeded.",
                "Err":   "The error message if things go wrong."}
    return jsonify(**response)

if __name__ == "__main__":
    app.run()
