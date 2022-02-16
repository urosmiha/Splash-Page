from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/splash", methods=["GET"])
def get_click():
    global base_grant_url
    global user_continue_url
    global success_url
    global client_ip
    global client_mac

    host = request.host_url
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac')
    splashclick_time = request.args.get('splashclick_time')
    success_url = host + "success"

    return render_template("index.html", client_ip=client_ip,
    client_mac=client_mac, node_mac=node_mac,
    user_continue_url=user_continue_url,success_url=success_url)


if __name__ == "__main__":
    # Hosted on localhost port 5004 - Remember to run "ngrok http 5004"
    app.run(host="0.0.0.0", port=5004, debug=False)