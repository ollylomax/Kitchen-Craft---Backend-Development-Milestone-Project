import os

# Import flask
from flask import Flask

# Import env file only if path exists
if os.path.exists("env.py"):
    import env

# Create instance of flask
app = Flask(__name__)


@app.route("/")
def functional():
    return "functional"


# Where and how to run out app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)