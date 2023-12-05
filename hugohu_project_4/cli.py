import json
import os
from urllib import request

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
API_TOKEN = os.getenv("API_TOKEN")

HEADERS = {"Authorization": "Bearer {}".format(API_TOKEN)}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"


@app.route("/")
def index():
    return render_template("index.html")


def query(payload):
    # response = requests.post(API_URL, headers=HEADERS, json=payload)
    # return json.loads(response.content.decode("utf-8"))[0]["summary_text"]
    json_payload = json.dumps(payload).encode("utf-8")
    req = request.Request(
        API_URL, data=json_payload, headers=HEADERS, method="POST"
    )

    with request.urlopen(req) as response:
        response_content = response.read().decode("utf-8")
        result = json.loads(response_content)
        return result[0]["summary_text"]


@app.route("/summarize", methods=["POST"])
def summarize():
    if request.method == "POST":
        user_input = request.form["user_input"]

        output = query(
            {
                "inputs": user_input,
            }
        )

        # Render the page with the result
        return render_template(
            "index.html", user_input=user_input, result=output
        )


def main():
    app.run(debug=False, host="0.0.0.0", port=80)
