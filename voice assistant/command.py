import pyttsx3
import datetime
import smtplib
import shutil
import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Jarvis")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


def record_audio(duration=5, fs=44100):
    """
    Record audio from the microphone using sounddevice.

    Args:
    duration (int): Duration of recording in seconds.
    fs (int): Sampling rate in Hz.

    Returns:
    numpy.ndarray: Recorded audio data.
    """
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")
    return audio_data


def save_audio(filename, audio_data, fs):
    """
    Save the recorded audio data to a WAV file.

    Args:
    filename (str): The path to the output file.
    audio_data (numpy.ndarray): The audio data to save.
    fs (int): Sampling rate in Hz.
    """
    wav.write(filename, fs, audio_data)


def takeCommand():
    """
    Capture and recognize audio from the microphone.

    Returns:
    str: The recognized text.
    """
    r = sr.Recognizer()
    fs = 44100  # Sampling rate
    duration = 5  # Duration of recording in seconds

    # Record audio
    audio_data = record_audio(duration, fs)

    # Save to file
    filename = "temp.wav"
    save_audio(filename, audio_data, fs)

    # Use speech_recognition to recognize the audio
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"
        return query
