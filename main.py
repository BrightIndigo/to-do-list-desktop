from winotify import Notification, audio
import time
import playsound

def wiadomosc():
    toast = Notification(app_id="Bruh",
                         title="Message Title",
                         msg= "Hi!",
                         duration="long",
                         icon=r"D:\Dokumenty\Photos\ytlogo.png")

    toast.set_audio(audio.LoopingAlarm, loop=False)

    toast.add_actions(label="Click Me!", launch="https://www.python.org/")

    toast.show()

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        if seconds_left < 10:
            seconds_left = "0" + str(seconds_left)

        if minutes_left < 10:
            minutes_left = "0" + str(minutes_left)

        print(f"{minutes_left}:{seconds_left}")

    wiadomosc()

sec = int(input("podaj ilość sekund do uruchomienia budzika: "))

alarm(sec)