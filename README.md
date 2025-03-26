# Voice Chatbot with OpenAI

## Overview
This is a voice-enabled chatbot powered by OpenAI's GPT-4o. It allows users to speak their queries, transcribes them to text, generates AI responses, and then converts the responses back to speech. The interaction feels natural and seamless, making it a great example of integrating voice-based AI conversations.

## Features
- Voice Input: Speak directly into your microphone.
- Speech-to-Text: Converts recorded speech into text using Google Speech Recognition.
- AI-Powered Chat: Sends the transcribed text to OpenAI's GPT-4o and retrieves a response.
- Text-to-Speech: Converts the AI response back into spoken words using gTTS.
- Audio Playback: Plays the AI-generated response using pygame.

## Installation
To run this chatbot locally, you need Python and some required dependencies.

### 1. Clone the repository:
```sh
git clone https://github.com/koderhydra1001/voice_chatbot.git
cd voice-chatbot
```

### 2. Install dependencies:
```sh
pip install -r requirements.txt
```

### 3. Set up OpenAI API Key:
Replace the following line in the code with your actual API key:
```python
openai.api_key = "your_api_key_here"
```

## Running the App
Run the chatbot using Streamlit:
```sh
streamlit run app.py
```

## How It Works
1. Click the 'Speak Now' button.
2. The app records your voice for 5 seconds.
3. It transcribes the audio into text.
4. The transcribed text is sent to OpenAI's GPT-4o.
5. The AI-generated response is converted into speech.
6. You hear the response played back to you.

## Troubleshooting
- Permission Error on Audio File: If the response audio doesn’t play, ensure no other program is using the file.
- Google Speech API Issues: Check your internet connection.
- OpenAI API Errors: Ensure your API key is valid and has enough credits.

## Future Enhancements
- Continuous conversation mode.
- Support for multiple languages.
- Deploy as a web-based chatbot.

## Contributing
Feel free to fork this project and improve it. Pull requests are welcome.

## License
This project is open-source under the MIT License.

---
Try it out and let your voice be heard.

