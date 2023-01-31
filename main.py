from flask import Flask, request, render_template, redirect
import sys

# Define global variables to be used across functions
global base_grant_url
base_grant_url = ""
global user_continue_url
user_continue_url = ""
global success_url
success_url = ""
global client_ip
client_ip = ""
global client_mac
client_mac = ""
global node_mac
node_mac = ""
global node_id
node_id = ""
global gateway_id
gateway_id = ""
global user_name
user_name = ""

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_main():
    """
        Simply redirect from main URL to splash page.
    """
    print("Here...", file=sys.stderr)

    return ''


@app.route("/clickthrough", methods=["GET"])
def get_splash():
    """
        This URL should be used when you enable CLICK THROUGH Splash Page access on Meraki dashboard.

        When client gets redirected to custom splash page, 
        Meraki Cloud would also include additional parameters in the URL.

        We can extract those and use them to display information.
    """

    global base_grant_url
    global user_continue_url
    global node_mac
    global node_id
    global gateway_id
    global client_ip
    global client_mac

    # extract all parameters when users connects to the splash page
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    node_id = request.args.get('node_id')
    gateway_id = request.args.get('gateway_id')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac')
    splashclick_time = request.args.get('splashclick_time')

    print(base_grant_url, file=sys.stderr)
    print(user_continue_url, file=sys.stderr)
    print(node_mac, file=sys.stderr)
    print(node_id, file=sys.stderr)
    print(gateway_id, file=sys.stderr)
    print(client_ip, file=sys.stderr)
    print(client_mac, file=sys.stderr)

    return render_template("index.html", base_grant_url=base_grant_url, client_ip=client_ip,
    client_mac=client_mac, node_mac=node_mac, node_id=node_id, gateway_id=gateway_id,
    user_continue_url=user_continue_url)


@app.route("/login", methods=["POST"])
def get_login():
    """ 
        For getting information when user completes splash page.
        It will capture information and redirect user to success or fail page.
    """

    # print('Login...')

    global user_name

    user_name = request.form['user_name']
    user_email = request.form['user_email']
    user_phone = request.form['user_phone']
    user_age = request.form['user_age']

    print(user_name, file=sys.stderr)
    print(user_email, file=sys.stderr)
    print(user_phone, file=sys.stderr)
    print(user_age, file=sys.stderr)

    return redirect("/success")


@app.route("/success",methods=["GET"])
def get_success():
    """
        Successful log-in.
        
        Let client confirm by clicking continue.
        Once they continue grant them access by sending base_grant_url back to Meraki.
        It's IMPORTANT that you include base_grant_url and continue URL, otherwise client won't get access to the network.
    """
    global base_grant_url
    global user_continue_url
    global user_name

    # You can leverage this to make changes to the continue_url (e.g where user will be redirected)
    # This can be used for targeted marketing or relevant info based on user input on the captive portal page.
    override_continue_url = "https://meraki.com"

    if user_name == "mrdiy":
        override_continue_url = "https://www.mrdiy.com/sg/promotion/"

    # Otherwise, just use the same url user was trying to get to in the first place
    # override_continue_url = user_continue_url

    # You can also specify how long user can be logged in for (in seconds)
    duration = 3600

    success_url = "{bsu}?continue_url={cu}&duration={d}".format(bsu=base_grant_url, cu=override_continue_url, d=duration)

    print(success_url, file=sys.stderr)

    return render_template("success.html", success_html=success_url)


@app.route("/denied",methods=["GET"])
def get_denied():
    return "Access denied... Contact administrator"


if __name__ == "__main__":
    # Hosted on localhost port 5004 - Remember to run "ngrok http 5004"
    # app.run(host="127.0.0.1", port=5004, debug=False)
    app.run(host="0.0.0.0", port=5004, debug=False)