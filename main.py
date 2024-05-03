import time
from winotify import Notification, audio

toast = Notification(app_id="Bruh",
                     title="Message Title",
                     msg= "Hi!",
                     duration="long",
                     icon=r"D:\Dokumenty\Photos\ytlogo.png")

toast.set_audio(audio.LoopingAlarm, loop=False)

toast.add_actions(label="Click Me!", launch="https://www.python.org/")

toast.show()
