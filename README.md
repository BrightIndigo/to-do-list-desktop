To-Do List Application Overview

This project is a feature-rich To-Do List application built using Python. The application leverages customtkinter for the GUI, winotify for sending Windows notifications, and tkcalendar for calendar integration. The app provides users with functionalities to manage tasks, set priorities, and schedule notifications with countdown timers. It is designed with a dark theme and allows users to switch between system and dark modes.

Features

Task Management:

Add tasks with different priority levels: Important, Average, Negligible.
Set due dates for tasks using an integrated calendar.
View tasks and their respective due dates, which are highlighted on the calendar.
Notification Timer:

Set customizable notifications with a title and message.
Configure a countdown timer that triggers notifications.
Dark Mode:

The application uses a dark theme by default.
Option to switch between system mode and dark mode.
Full-Screen Window:

The application runs in a windowed full-screen mode for better user experience.
Getting Started
Prerequisites
Ensure you have Python installed on your machine. The required Python libraries are:

customtkinter
winotify
tkcalendar

You can install these libraries using pip:

pip install customtkinter winotify tkcalendar
Running the Application
Clone the repository or copy the code to your local machine.
Ensure the required libraries are installed.

Run the application using:

python your_script_name.py
Application Interface
Upon running the application, the following features are available from the main menu:

Set Notification Timer: 

Allows users to set a custom notification with a countdown timer.

Add Tasks: 

Enables adding tasks with specific priorities and due dates.

View Tasks: 

Displays all tasks along with their respective due dates on a calendar.

File Storage:

Tasks are stored in a tasks.txt file in the format: [Priority] [Task Description] [Due Date].

How to Use

Adding a Task
Click on the "Add Tasks" button.
Select the priority of your task.
Write the task description in the text box.
Choose the due date using the calendar widget.
Click "Confirm" to save the task.

Viewing Tasks

Click on the "View Tasks" button.
The calendar will display the due dates of tasks.
Each task is listed with its priority, description, and due date.

Setting a Notification Timer

Click on the "Set Notification Timer" button.
Enter a title and message for the notification.
Set the countdown timer by specifying hours, minutes, and/or seconds.
Click "Start the countdown" to begin the timer. A notification will appear when the countdown ends.

Changing Themes

Use the "Change theme" switch to toggle between the dark mode and system mode.
Future Enhancements
Implement task editing and deletion functionality.
Add recurring task reminders.
Enhance the notification system with more customizable options.
License
This project is licensed under the MIT License - see the LICENSE file for details.

