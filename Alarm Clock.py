from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox
import datetime
from time import strftime
from pygame import mixer
from PIL import Image, ImageTk
from pygame.threads import Thread

# Window
root = Tk()
root.title('Shik Alarm')
root.geometry('375x200')
font.families()  # Tkinter fonts first import font from tkinter.

selected = IntVar()

# Alarm
def start_alarm():
    s = Thread(target=alarm)
    s.start()


def stop_alarm():
    print('Alarm is stopped', selected.get())
    mixer.music.stop()


def sound_alarm():
    mixer.music.load('Alarm_sing.mp3')  # <<<< You can load here what do u want to sing music.
    mixer.music.play()
    selected.set(0)


def time_show():
    time_string = strftime('%H:%M:%S')
    time.config(text=time_string)
    time.after(1000, time_show)

def date_show():
    date_string = strftime('%d/%m/%Y')
    date.config(text=date_string)
    date.after(86400000, date_show)

def alarm():
    global second, hour, minute
    while True:
        control = 1
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_minute.get()
        alarm_second = c_second.get()

        current_time = datetime.datetime.now()

        hour = current_time.strftime('%H')
        minute = current_time.strftime('%M')
        second = current_time.strftime('%S')

        if control == 1:
            if alarm_hour == hour:
                if alarm_minute == minute:
                    if alarm_second == second:
                        print('''
                        Time is up
                        Time is up
                        Time is up
                        Time is up
                        Time is up
                        ''')
                        sound_alarm()
                        break


# Frame
main_frame = Frame(root, width=400, height=290)
main_frame.grid(row=0, column=0)

# Image option
img = Image.open('Alarm_icon.png')  # <<<< You can add your image from here.
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

# Image place
alarm_image = Label(root, height=100, image=img)
alarm_image.place(x=0, y=30)

# Clock names
alarm_name = Label(main_frame, text='Shik Alarm', height=1, font='Courier 18')  # <<<< You can change Alarm name here.
alarm_name.place(x=145, y=4)

hour = Label(main_frame, text='Hour', height=1, font='Courier 10 bold')
hour.place(x=137, y=58)

minute = Label(main_frame, text='Minute', height=1, font='Courier 10 bold')
minute.place(x=198, y=58)

second = Label(main_frame, text='Second', height=1, font='Courier 10 bold')
second.place(x=262, y=58)


# Hour
c_hour = Combobox(main_frame, width=2, font='Courier 15 ', state='readonly')
c_hour.place(x=133, y=75)
c_hour['values'] = (
 '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
 '20', '21', '22', '23', '24')
c_hour.current(0)

# Minute
c_minute = Combobox(main_frame, width=2, font='Courier 15', state='readonly')
c_minute.place(x=200, y=75)
c_minute['values'] = (
 '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
 '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
 '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_minute.current(0)

# Second
c_second = Combobox(main_frame, width=2, font='Courier 15', state='readonly')
c_second.place(x=267, y=75)
c_second['values'] = (
 '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
 '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
 '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_second.current(0)

# Buttons
rad1 = Radiobutton(main_frame, text='Start', value=1, font='Courier 9 bold', width=10,
                   relief=RAISED, command=start_alarm, variable=selected)

rad1.place(x=125, y=140)

rad2 = Radiobutton(main_frame, text='Stop', value=2, font='Courier 9 bold', width=10,
                   relief=RAISED, command=stop_alarm, variable=selected)

rad2.place(x=224, y=140)

# Date
date = Label(main_frame, font='Courier 9 ')
date.place(x=0, y=0)

# Time
time = Label(main_frame, font='Courier 10 ')
time.place(x=305, y=0)


date_show()
time_show()
mixer.init()

mainloop()
