from flask import Flask
import os
from pyaml_env import parse_config


app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask inside Docker!!"

@app.route("/health/ping")
def healthCheck():
    return "Flask is up and running"

@app.route("/v1/config/all")
def configGet():
    TEST_INT_VALUE = os.environ["TEST_INT_VALUE"]
    config = parse_config('prop.yaml')
    print(config["testSecret1FromSM"])
    return config


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
