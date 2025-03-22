from flask import Flask, request, jsonify
from agent import main  # This should have respond_to_query function

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_agent():
    """
    This endpoint receives JSON data from frontend,
    sends the 'message' to the AI agent, and returns response.
    """
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({"error": "No message provided"}), 400

    response = main.respond_to_query(message)
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)
