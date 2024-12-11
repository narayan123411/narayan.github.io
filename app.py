from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
# Rasa server URL (make sure this is where your Rasa server is running)
RASA_SERVER_URL = "http://127.0.0.1:5005/webhooks/rest/webhook"

@app.route('/')
def index():
    return render_template('chatbox.html')

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
    app.run(debug=True, port=5000)


