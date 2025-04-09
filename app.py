from flask import Flask, render_template, request, jsonify
from buddy_ai import BuddyAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
buddy = BuddyAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    # Generate response from BUDDY
    response = buddy.generate_response(user_message)
    
    # Get current platform and focus area from session
    platform = buddy.user_session.get('platform')
    focus_area = buddy.user_session.get('focus_area')
    
    return jsonify({
        'response': response,
        'platform': platform,
        'focus_area': focus_area
    })

@app.route('/api/voice', methods=['POST'])
def voice():
    # This endpoint would handle voice input
    # For now, it's a placeholder
    return jsonify({'status': 'not implemented yet'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) 