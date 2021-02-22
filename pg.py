import speech_recognition as sr
import moviepy.editor as mp

clip = mp.VideoFileClip(r"whatisAI.mp4")
clip.audio.write_audiofile(r"transfer.wis")
r = sr.Recognizer()
audio = sr.AudioFile("transfer.wis")
with audio as source:
    audio_file = r.record(source)
    result = r.recognize_google(audio_file)
with open('recognized.txt', mode='wt') as audio_file:
file.write("recognized speech:")
file.write("\n")
file.write(result)
print('ready')