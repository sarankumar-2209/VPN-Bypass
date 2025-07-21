from flask import Flask, request, render_template
import datetime
import os

app = Flask(__name__)

LOG_FILE = "logs.txt"

@app.route('/')
def index():
    # Get IP and headers
    remote_ip = request.remote_addr
    forwarded_ip = request.headers.get("X-Forwarded-For")
    real_ip = request.headers.get("X-Real-IP")
    user_agent = request.headers.get("User-Agent", "Unknown")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"""
[+] New Visitor - {now}
Remote IP        : {remote_ip}
X-Forwarded-For  : {forwarded_ip}
X-Real-IP        : {real_ip}
User-Agent       : {user_agent}
---------------------------------------------------
"""

    print(log_entry)

    # Save to file
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    return render_template('index.html',
                           remote_ip=remote_ip,
                           forwarded_ip=forwarded_ip,
                           real_ip=real_ip,
                           user_agent=user_agent)
