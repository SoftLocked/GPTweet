from flask import Flask, render_template, request, flash
import os
import openai
import json
from urllib.parse import quote



app = Flask(__name__)
app.secret_key = "jfkdlasfjkldsa"




@app.route("/")
def home():
    flash("Output will appear here...")
    return render_template("index.html")


@app.route("/output_tweet", methods=["POST", "GET"])
def output_success():
    with open("secrets.json", ) as f:
        openai.api_key = json.load(f)["GPT-key"]

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": f"Write me a tweet reacting to the following information: {str(request.form['data_stream'])}"}],
                                                   max_tokens=60)

    #print(chat_completion)
    chat_response = chat_completion["choices"][0]["message"]["content"][1:-1]

    response_encoded = quote(chat_response)

    flash(chat_response)
    flash(response_encoded)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)