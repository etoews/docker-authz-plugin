from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def index():
    return "Docker Authz Plugin"

@app.route("/Plugin.Activate")
def activate():
    return jsonify({'Implements': ['authz']})

@app.route("/AuthzPlugin.AuthZReq")
def authz_request():
    print("AuthZ Request")
    print(request.data)
    r = {"Allow": True,
         "Msg":   "The request authorization message",
         "Err":   "The error message if things go wrong"}
    return jsonify(**r)

@app.route("/AuthzPlugin.AuthZRes")
def authz_response():
    print("AuthZ Response")
    print(request.data)
    r = {"Allow": True,
         "Msg":   "The response authorization message",
         "Err":   "The error message if things go wrong"}
    return jsonify(**r)

if __name__ == "__main__":
    app.run()
