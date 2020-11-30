import pyttsx3
from datetime import datetime, date, time

tts = pyttsx3.init()
tts.setProperty('voice', 'ru')  # голос по умолчанию
tts.setProperty('rate', 150)  # скорость в %
tts.setProperty('volume', 0.8)  # громкость от 0 до 1

voices = tts.getProperty('voices')
for voice in voices:
    print(voice.id)

for voice in voices:
    if 'Irina' in voice.name:
        tts.setProperty('voice', voice.id)


def say_time(s):
    tts.say(s)
    tts.runAndWait


time_checker = datetime.now()
say_time(f'{time_checker.hour} часов {time_checker.minute} минут')
