# speech_app/utils.py
import speech_recognition as sr
from pydub import AudioSegment
import os

# def speech_to_text(audio_file):
#     # Convert mp3 file to wav
#     sound = AudioSegment.from_file(audio_file, format="mp3")
#     wav_path = "temp.wav"
#     sound.export(wav_path, format="wav")

#     # Use the converted wav file
#     r = sr.Recognizer()
#     with sr.AudioFile(wav_path) as source:
#         audio = r.record(source)  # read the entire audio file

#     # Attempt to recognize the speech
#     try:
#         result = r.recognize_google(audio)
#     except sr.UnknownValueError:
#         result = "Google Speech Recognition could not understand audio"
#     except sr.RequestError as e:
#         result = f"Could not request results from Google Speech Recognition service; {e}"

#     # Clean up the temporary wav file
#     os.remove(wav_path)

#     return result


# def speech_to_text(audio_file):
#     # Convert mp3 file to wav
#     sound = AudioSegment.from_file(audio_file, format="mp3")
#     wav_path = "temp.wav"
#     sound.export(wav_path, format="wav")

#     r = sr.Recognizer()
#     with sr.AudioFile(wav_path) as source:
#         r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust based on the first 0.5 seconds
#         audio = r.record(source)

#     try:
#         result = r.recognize_google(audio)
#     except sr.UnknownValueError:
#         result = "Google Speech Recognition could not understand audio"
#     except sr.RequestError as e:
#         result = f"Could not request results from Google Speech Recognition service; {e}"

#     os.remove(wav_path)
#     return result

# speech_app/utils.py
import os
from pydub import AudioSegment
import speech_recognition as sr





# speech_app/utils.py
import string

def normalize_text(text):
    # Remove punctuation using a translation table and convert to lowercase
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def speech_to_text(audio_file):
    # Your existing speech_to_text function
    pass



def speech_to_text(audio_file):
    # Convert mp3 file to wav
    sound = AudioSegment.from_file(audio_file, format="mp3")
    wav_path = "temp.wav"
    sound.export(wav_path, format="wav")

    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)  # read the entire audio file

    # Attempt to recognize the speech
    try:
        result = r.recognize_google(audio)
    except sr.UnknownValueError:
        result = "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        result = f"Could not request results from Google Speech Recognition service; {e}"

    # Comment this out to check if 'temp.wav' exists
    # os.remove(wav_path)

    return result
