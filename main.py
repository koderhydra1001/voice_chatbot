import openai
import streamlit as st
import sounddevice as sd
import numpy as np
import wavio
import speech_recognition as sr
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import pygame
import time

openai.api_key = "please enter your OpenAI key"

def record_audio(filename="input.wav", duration=5, samplerate=44100):
    st.info("🎤 Recording... Speak now!")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    wavio.write(filename, audio, samplerate)
    st.success("✅ Recording complete! Transcribing now...")
    return filename

def transcribe_audio(filename="input.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "❌ Could not understand the audio."
    except sr.RequestError:
        return "❌ Could not connect to Google API."

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful AI voice assistant."}, 
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def text_to_speech(response_text):
    tts = gTTS(response_text)
    audio_path = "response.mp3"
    
    # Stop and unload previous audio file if it's playing
    pygame.mixer.init()
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    # Ensure the old file is deleted before saving
    if os.path.exists(audio_path):
        try:
            os.remove(audio_path)  # Delete previous file
            time.sleep(1)  # Short delay to ensure file is released
        except PermissionError:
            print("File in use, retrying after delay...")
            time.sleep(2)  # Wait longer before retrying
            os.remove(audio_path)

    # Save new audio file
    tts.save(audio_path)

    # Load and play the new file
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(2)

    return audio_path


st.title("🎙️ Voice Chatbot with OpenAI")
st.write("Click the button below, speak your question, and hear the response.")

if st.button("🎤 Speak Now"):
    audio_file = record_audio()
    user_query = transcribe_audio(audio_file)
    
    st.write(f"**You said:** {user_query}")
    
    if user_query and "❌" not in user_query:
        bot_response = chat_with_gpt(user_query)
        st.write(f"🤖 **ChatGPT:** {bot_response}")
        
        audio_file = text_to_speech(bot_response)
        st.audio(audio_file, format="audio/mp3")

st.write("🔊 This bot responds in voice! Try asking a question.")
