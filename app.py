import os
from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

RASA_SERVER_URL = os.environ.get("RASA_SERVER_URL", "http://127.0.0.1:5005/webhooks/rest/webhook")

@app.route('/')
def index():
    return send_file('chatbox.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    data = request.json
    print(f"Received data: {data}")
    
    # Send the user's message to the Rasa server
    response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
    print(response)
    # Get the bot's reply
    if response.status_code == 200:
        bot_messages = response.json()
        print(f"Bot messages: {bot_messages}")
        #text = bot_message[0].get('text')
        
    else:
        bot_messages = [{"text": "Sorry, something went wrong."}]
    
    return jsonify(bot_messages)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
