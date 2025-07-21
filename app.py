from flask import Flask, request, render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
    remote_ip = request.remote_addr
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    x_real_ip = request.headers.get("X-Real-IP")
    user_agent = request.headers.get("User-Agent")
    return render_template("index.html", remote_ip=remote_ip,
                           x_forwarded_for=x_forwarded_for,
                           x_real_ip=x_real_ip,
                           user_agent=user_agent)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
