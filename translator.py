import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def get_input_mode():
    print("Choose input mode:\n1. Speech\n2. Text")
    return input("Enter your choice (1 or 2): ")

def get_language_choice():
    print("Choose language:\n1. English\n2. Tamil")
    return input("Enter your choice (1 or 2): ")

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

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")

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
