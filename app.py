from flask import Flask, render_template
from datetime import datetime
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        version=os.getenv("APP_VERSION", "v1.0.0"),
        environment=os.getenv("ENVIRONMENT", "Production"),
        image=os.getenv("IMAGE_TAG", "latest"),
        current_time=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
