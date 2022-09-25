
from flask import Flask, request
import os
import openai
from flask_cors import CORS

app = Flask(__name__)
openai.api_key ="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"
CORS(app)
@app.route('/')
def home_view():
        return "<h1>GPT-3 APIs are working :)</h1>"
@app.route("/test_prompt", methods=["POST"])
def test_prompt():
    prompt = request.get_json().get("prompt")
    return complete_prompt(prompt) 

def complete_prompt(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt='What are 5 key points I should know when studying '+prompt+"?",
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Get and return just the text response
    return response["choices"][0]["text"]


@app.route('/tweet', methods=['POST'])
def tweet():
    prompt = request.get_json().get("prompt")
    return tweet_prompt(prompt)
def tweet_prompt(prompt):

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Classify the sentiment in these tweets: "+prompt+" Tweet sentiment ratings:",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
)
# Get and return just the text response
    print(response["choices"])
    return response["choices"][0]["text"]

    