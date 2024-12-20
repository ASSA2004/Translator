# Translator

Speech-to-Text, Translation, and Text-to-Speech System

Project Overview

This project is a Python-based application that enables users to input text either via speech or typing, translate it between English and Tamil, and hear the translated output as speech. It leverages multiple Python libraries to handle speech recognition, language translation, and text-to-speech synthesis.

Features

Speech Input: Users can input text by speaking into a microphone.
Text Input: Users can manually type text for translation.
Language Translation: Supports translation between English and Tamil.
Text-to-Speech: Converts the translated text into speech and plays it.
Technology Stack

Python
Libraries:
speech_recognition for speech-to-text conversion.
googletrans for language translation.
gTTS for text-to-speech conversion.
os for interacting with the operating system to play audio files.

Code Breakdown

1. Importing Libraries

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

speech_recognition: Handles speech input.
googletrans: Provides translation functionality.
gTTS: Converts text to speech.
os: Manages file operations and system commands.

2. Input Mode Selection

def get_input_mode():
    print("Choose input mode:\n1. Speech\n2. Text")
    return input("Enter your choice (1 or 2): ")

Prompts the user to select between speech and text input modes.

3. Language Selection

def get_language_choice():
    print("Choose language:\n1. English\n2. Tamil")
    return input("Enter your choice (1 or 2): ")

Prompts the user to select the source language: English or Tamil.

4. Speech Recognition

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

Captures audio from the microphone, recognizes it using Google’s Speech Recognition API, and returns the recognized text.

5. Translation

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

Translates the input text from the source language to the target language using Google Translate.

6. Text-to-Speech Conversion

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")

Converts the translated text into speech and plays it using the system’s default media player.

7. Main Workflow

def main():
    input_mode = get_input_mode()
    source_lang_choice = get_language_choice()

    source_lang = 'en' if source_lang_choice == '1' else 'ta'
    target_lang = 'ta' if source_lang_choice == '1' else 'en'

    if input_mode == '1':  # Speech input
        print(f"Speak in {'English' if source_lang == 'en' else 'Tamil'}...")
        text = recognize_speech()
    else:  # Text input
        text = input(f"Enter your {'English' if source_lang == 'en' else 'Tamil'} text: ")

    if text:
        translated_text = translate_text(text, source_lang, target_lang)
        print(f"Original text: {text}")
        print(f"Translated text: {translated_text}")
        text_to_speech(translated_text, target_lang)

if __name__ == "__main__":
    main()

The main function orchestrates the flow:
Prompts the user for input mode and language choice.
Captures input (speech or text).
Translates the input text to the target language.
Converts the translated text to speech and plays it.
Usage Instructions

Install the required libraries:
pip install speechrecognition googletrans==4.0.0-rc1 gTTS

Run the script:
python script_name.py

Follow the on-screen instructions to:
Select input mode (speech or text).
Select the source language (English or Tamil).
Provide input as speech or text.
Listen to the translated speech output.

Future Enhancements
Support for additional languages.
Improved error handling for translation and speech recognition.
Integration with a GUI for better usability.

Conclusion
This project demonstrates the integration of speech recognition, language translation, and text-to-speech technologies to create a user-friendly application that bridges language barriers.
