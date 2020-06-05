import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander


def say(text):
    subprocess.call('echo ' + text + ' | "C:\Program Files\Jampal\ptts.vbs"', shell=True)

def play_audio(filename):
    chunk = 1024  # chunk size
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )
    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening..")
    play_audio('audio/sound.wav')
    with sr.Microphone() as source:
        print("Say something..")
        audio = r.listen(source)
    play_audio("./audio/sound.wav")
    command = ""

    try:
        command = r.recognize_google(audio)  # using google to do speech-to-text
        print(command)
        print("wait... responding")
    except:
        command = "Couldn't understand you"

    if command in cmd.exit:
        Running = False
        cmd.respond("Okay. Bye for now. Talk to you soon!")
    elif command is "Couldn't understand you":
        cmd.respond("Couldn't understand you")
    else:
        cmd.discover(command)

Running = True
while Running is True:
    initSpeech()
