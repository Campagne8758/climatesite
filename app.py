from flask import Flask, flash, redirect, render_template, request, session
from helpers import temp_anomaly

app = Flask(__name__)

@app.route("/")
def index():
    #  get ip address for future use to get user's location
    ip_address = request.remote_addr
    tmp_display = temp_anomaly(50, 1)
    return render_template("index.html", tmp_display=tmp_display, ip_address=ip_address)
