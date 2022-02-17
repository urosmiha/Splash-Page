from flask import Flask, request, render_template, redirect
import sys

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_main():
    """
        Simply redirect from main URL to splash page.
    """
    return redirect("/splash")


@app.route("/splash", methods=["GET"])
def get_splash():
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


@app.route("/login", methods=["POST"])
def get_login():
    """ 
        For getting information when user completes splash page.
        It will capture information and redirect user to success or fail page.
    """

    # print('Login...')

    user_name = request.form['user_name']
    user_email = request.form['user_email']
    user_phone = request.form['user_phone']
    user_company = request.form['user_company']

    print(user_name, file=sys.stderr)
    print(user_email, file=sys.stderr)
    print(user_phone, file=sys.stderr)
    print(user_company, file=sys.stderr)

    return redirect("/success")


@app.route("/success",methods=["GET"])
def get_success():
    """
        Successful log-in.
    """

    print("Success", file=sys.stderr)

    return render_template("success.html")


@app.route("/denied",methods=["GET"])
def get_denied():
    return "Access denied... Contact administrator"


if __name__ == "__main__":
    # Hosted on localhost port 5004 - Remember to run "ngrok http 5004"
    app.run(host="127.0.0.1", port=5004, debug=False)