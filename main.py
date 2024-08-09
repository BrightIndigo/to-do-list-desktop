import time
from winotify import Notification, audio
import customtkinter as ctk
from threading import Thread
from tkcalendar import Calendar, DateEntry
from datetime import datetime

def set_windowed_fullscreen(root):
    root.state('zoomed')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

app = ctk.CTk()
set_windowed_fullscreen(app)
app.title("To do list")
ctk.set_appearance_mode("dark")
color_palette = ["#9d0c1d", "#851e13", "#50120a", "#2b1507", "#19180a"]
def gui_setup():
    for widget in app.winfo_children():
        widget.destroy()

    def Set_notification_window():
        for widget in app.winfo_children():
            widget.destroy()

        button_gui_setup = ctk.CTkButton(master=app, text="Menu", command=gui_setup, width=200, height=50, fg_color=color_palette[2], corner_radius=20, hover_color=color_palette[1])
        button_gui_setup.pack(padx=20, pady=10)

        text_var_title = ctk.StringVar(value="Set a title")

        label_title = ctk.CTkLabel(master=app,
                             textvariable=text_var_title,
                             width=120,
                             height=25,
                             corner_radius=8)
        label_title.pack(padx=5, pady=5)

        entry_title = ctk.CTkEntry(master=app,
                                     placeholder_text="Title",
                                     width=120,
                                     height=25,
                                     border_width=2,
                                     corner_radius=10
                                     )
        entry_title.pack(padx=5, pady=5)

        text_var_message = ctk.StringVar(value="Set a message")

        label_message = ctk.CTkLabel(master=app,
                             textvariable=text_var_message,
                             width=120,
                             height=25,
                             corner_radius=8)
        label_message.pack(padx=5, pady=5)

        entry_message = ctk.CTkEntry(master=app,
                                   placeholder_text="Message",
                                   width=120,
                                   height=25,
                                   border_width=2,
                                   corner_radius=10
                                   )
        entry_message.pack(padx=5, pady=5)


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
        label.pack(padx=5, pady=5)

        entry_hours = ctk.CTkEntry(master=app,
                             placeholder_text="Hours",
                             width=75,
                             height=75,
                             border_width=2,
                             corner_radius=10)
        entry_hours.place(relx=0.46, rely=0.25, anchor=ctk.CENTER)

        entry_minutes = ctk.CTkEntry(master=app,
                                   placeholder_text="Minutes",
                                   width=75,
                                   height=75,
                                   border_width=2,
                                   corner_radius=10)
        entry_minutes.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        entry_seconds = ctk.CTkEntry(master=app,
                                   placeholder_text="Seconds",
                                   width=75,
                                   height=75,
                                   border_width=2,
                                   corner_radius=10
                                   )
        entry_seconds.place(relx=0.54, rely=0.25, anchor=ctk.CENTER)


        button_alarm_start = ctk.CTkButton(master=app, text="Start the countdown", command=alarm_start, fg_color=color_palette[2], corner_radius=20, hover_color=color_palette[1])
        button_alarm_start.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

    def change_theme():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("system")
        else:
            ctk.set_appearance_mode("dark")

    switch_var = ctk.StringVar(value="off")
    switch_change_theme = ctk.CTkSwitch(master=app, text="Change theme", command=change_theme, variable=switch_var, onvalue="on", offvalue="off")
    switch_change_theme.pack(padx=20, pady=10)

    notification_timer_button = ctk.CTkButton(master=app,
                                              text="Set notification",
                                              command=Set_notification_window,
                                              corner_radius=20,
                                              border_width=1,
                                              border_color=color_palette[1],
                                              width=300,
                                              height=120,
                                              fg_color=color_palette[2],
                                              hover_color=color_palette[1],
                                              )
    notification_timer_button.pack(padx=20, pady=10)

    def add_tasks():
        for widget in app.winfo_children():
            widget.destroy()

        button_gui_setup = ctk.CTkButton(master=app, text="Menu", command=gui_setup, width=200, height=50, fg_color=color_palette[2], corner_radius=20, hover_color=color_palette[1])
        button_gui_setup.pack(padx=20, pady=10)

        label = ctk.CTkLabel(app, text="", fg_color="transparent", font=("Verdana", 18))
        label.pack(padx=20, pady=15)

        label = ctk.CTkLabel(app, text="Set priority of your task", fg_color="transparent", font=("Verdana", 18))
        label.pack(padx=20, pady=0)

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)
        optionmenu = ctk.CTkOptionMenu(app, values=["Important", "Average", "Negligible"],
                                       command=optionmenu_callback, fg_color=(color_palette[1]),
                                       button_color=color_palette[1], button_hover_color=color_palette[2])
        optionmenu.set("Important")
        optionmenu.pack(padx=20, pady=10)

        label = ctk.CTkLabel(app, text="", fg_color="transparent", font=("Verdana", 18))
        label.pack(padx=20, pady=15)

        label = ctk.CTkLabel(app, text="Write what you need to do", fg_color="transparent", font=("Verdana", 18))
        label.pack(padx=20, pady=0)

        entry = ctk.CTkEntry(app, placeholder_text="Type here", width=300, height=50)
        entry.pack(padx=20, pady=10)

        label = ctk.CTkLabel(app, text="", fg_color="transparent", font=("Verdana", 18))
        label.pack(padx=20, pady=15)

        label = ctk.CTkLabel(app, text="Choose day of your task", fg_color="transparent", font=("Verdana", 18))
        label.pack(padx=20, pady=0)

        #calendar
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        current_day = now.day

        def get_date():
            selected_date = cal.get_date()
            print("Selected Date is:", selected_date)

        cal = Calendar(app, selectmode='day', year=current_year, month=current_month, day=current_day, selectbackground=color_palette[1])
        cal.pack(padx=20, pady=10)
        button = ctk.CTkButton(app, text="Confirm", command=get_date, fg_color=color_palette[1], corner_radius=20, hover_color=color_palette[2])
        button.pack(padx=20, pady=10)





    tasks_button = ctk.CTkButton(master=app,
                                              text="Add tasks",
                                              command=add_tasks,
                                              corner_radius=20,
                                              border_width=1,
                                              border_color=color_palette[1],
                                              width=300,
                                              height=120,
                                              fg_color=color_palette[2],
                                              hover_color=color_palette[1],
                                              )
    tasks_button.pack(padx=20, pady=10)

    def view_tasks():
        for widget in app.winfo_children():
            widget.destroy()

    view_tasks_button = ctk.CTkButton(master=app,
                                              text="View tasks",
                                              command=view_tasks,
                                              corner_radius=20,
                                              border_width=1,
                                              border_color=color_palette[1],
                                              width=300,
                                              height=120,
                                              fg_color=color_palette[2],
                                              hover_color=color_palette[1],
                                              )
    view_tasks_button.pack(padx=20, pady=10)



gui_setup()
app.mainloop()
