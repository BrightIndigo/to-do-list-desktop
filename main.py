import time
from winotify import Notification, audio
import customtkinter as ctk
from threading import Thread

app = ctk.CTk()
app.geometry("1920x1080")
app.title("To do list")

def gui_setup():
    for widget in app.winfo_children():
        widget.destroy()

    def timer_window():
        for widget in app.winfo_children():
            widget.destroy()

        button_gui_setup = ctk.CTkButton(master=app, text="Menu", command=gui_setup)
        button_gui_setup.place(relx=0.5, rely=0.02, anchor=ctk.CENTER)

        text_var_title = ctk.StringVar(value="Set a title")

        label_title = ctk.CTkLabel(master=app,
                             textvariable=text_var_title,
                             width=120,
                             height=25,
                             corner_radius=8)
        label_title.place(relx=0.5, rely=0.07, anchor=ctk.CENTER)

        entry_title = ctk.CTkEntry(master=app,
                                     placeholder_text="Title",
                                     width=120,
                                     height=25,
                                     border_width=2,
                                     corner_radius=10
                                     )
        entry_title.place(relx=0.5, rely=0.095, anchor=ctk.CENTER)

        text_var_message = ctk.StringVar(value="Set a message")

        label_message = ctk.CTkLabel(master=app,
                             textvariable=text_var_message,
                             width=120,
                             height=25,
                             corner_radius=8)
        label_message.place(relx=0.5, rely=0.12, anchor=ctk.CENTER)

        entry_message = ctk.CTkEntry(master=app,
                                   placeholder_text="Message",
                                   width=120,
                                   height=25,
                                   border_width=2,
                                   corner_radius=10
                                   )
        entry_message.place(relx=0.5, rely=0.14, anchor=ctk.CENTER)


        def show_notification():

            if entry_title != "" and entry_message != "":

                toast = Notification(app_id="To do list",
                                     title=entry_title.get(),
                                     msg=entry_message.get(),
                                     duration="long"
                                     )

                toast.set_audio(audio.LoopingAlarm, loop=False)
                toast.add_actions(label="Click Me!", launch="https://www.python.org/")
                toast.show()

        def countdown(seconds):
            time_elapsed = 0
            while time_elapsed < seconds:
                time.sleep(1)
                time_elapsed += 1

                time_left = seconds - time_elapsed
                minutes_left = time_left // 60
                seconds_left = time_left % 60

                print(f"{minutes_left:02}:{seconds_left:02}")

            show_notification()

        def alarm_start():
            input_value_hours = entry_hours.get()
            input_value_minutes = entry_minutes.get()
            input_value_seconds = entry_seconds.get()
            if entry_title.get != "" and entry_message.get() != "":
                count_hours = False
                count_minutes = False
                count_seconds = False
                sec = 0

                if input_value_seconds.isnumeric() and input_value_seconds != "":
                    count_seconds = True
                    sec += int(input_value_seconds)
                if input_value_minutes.isnumeric() and input_value_minutes != "":
                    count_minutes = True
                    sec += int(input_value_minutes) * 60
                if input_value_hours.isnumeric() and input_value_hours != "":
                    count_hours = True
                    sec += int(input_value_hours) * 3600

                if count_seconds or count_minutes or count_hours:
                    if sec > 0:
                        Thread(target=countdown, args=(sec,)).start()
                    else:
                        print("Please enter a positive number.")
                else:
                    print("Please enter a valid number.")
            else:
                print("Complete the fields.")

        text_var_timer = ctk.StringVar(value="Set a timer")

        label = ctk.CTkLabel(master=app,
                             textvariable=text_var_timer,
                             width=120,
                             height=25,
                             corner_radius=8)
        label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        entry_hours = ctk.CTkEntry(master=app,
                             placeholder_text="Hours",
                             width=75,
                             height=75,
                             border_width=2,
                             corner_radius=10)
        entry_hours.place(relx=0.46, rely=0.55, anchor=ctk.CENTER)

        entry_minutes = ctk.CTkEntry(master=app,
                                   placeholder_text="Minutes",
                                   width=75,
                                   height=75,
                                   border_width=2,
                                   corner_radius=10)
        entry_minutes.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

        entry_seconds = ctk.CTkEntry(master=app,
                                   placeholder_text="Seconds",
                                   width=75,
                                   height=75,
                                   border_width=2,
                                   corner_radius=10
                                   )
        entry_seconds.place(relx=0.54, rely=0.55, anchor=ctk.CENTER)


        button_alarm_start = ctk.CTkButton(master=app, text="Start the countdown", command=alarm_start)
        button_alarm_start.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)


    def change_theme():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("system")
        else:
            ctk.set_appearance_mode("dark")

    switch_var = ctk.StringVar(value="on")
    switch_change_theme = ctk.CTkSwitch(master=app, text="Theme", command=change_theme, variable=switch_var, onvalue="on", offvalue="off")
    switch_change_theme.pack(padx=20, pady=10)

    notification_timer_button = ctk.CTkButton(master=app,
                                              text="Set notification",
                                              command=timer_window,
                                              corner_radius=20,
                                              border_width=1,
                                              border_color="white",
                                              width=300,
                                              height=120,
                                              )
    notification_timer_button.pack(padx=20, pady=10)



gui_setup()
app.mainloop()
