import random
from winotify import Notification, audio
import time
import playsound
import customtkinter as ctk
import random

def change_theme():
    if switch_var.get() == "on":
        ctk.set_appearance_mode("system")
    else:
        ctk.set_appearance_mode("dark")

def alarm_start():
    def wiadomosc():
        toast = Notification(app_id="Bruh",
                             title="Message Title",
                             msg="Hi!",
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

    if entry.get().isnumeric() and entry.get() != "":
        sec = int(entry.get())
        alarm(sec)



app = ctk.CTk()
app.geometry("1500x1080")
app.title("To do list desktop app")

button = ctk.CTkButton(master=app, text="Start the countdown", command=alarm_start)
button.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)


switch_var = ctk.StringVar(value="on")
switch_1 = ctk.CTkSwitch(master=app, text="Theme", command=change_theme,
                                   variable=switch_var, onvalue="on", offvalue="off")
switch_1.pack(padx=20, pady=10)

text_var = ctk.StringVar(value="Enter number of seconds to start alarm clock")

label = ctk.CTkLabel(master=app,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               corner_radius=8)
label.place(relx=0.5, rely=0.05, anchor=ctk.CENTER)



entry = ctk.CTkEntry(master=app,
                               placeholder_text="Enter number of seconds!",
                               width=200,
                               height=75,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)


app.mainloop()


