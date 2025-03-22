from flask import Flask, request
from agent import main

app = Flask(__name__)

@app.route('/slack', methods=['POST'])
def slack_endpoint():
    """
    This endpoint receives requests from Slack, extracts the text,
    sends it to the AI agent, and returns the response.
    """
    data = request.form
    text = data.get('text')
    if text:
        response = main.respond_to_query(text)
        return response
    else:
        return "No text found in Slack request."

if __name__ == '__main__':
    app.run(debug=True)
