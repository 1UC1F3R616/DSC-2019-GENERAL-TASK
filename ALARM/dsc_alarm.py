# -*- coding:utf-8 -*-

from tkinter import *
from pygame import mixer
from time import strftime
from datetime import datetime as dt
from tkinter import messagebox
import webbrowser

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

root = Tk()


def play_default_sound():
    global mixer
    mixer.init()
    mixer.music.load('alarm_tune.mp3')
    mixer.music.play()


def alarm_ring(hour_value, min_value, snooze_value,
               email_value, sound_value, link_value, on_off_value):
    global mixer

    hour_value = hour_value
    min_value = min_value
    snooze_value = snooze_value
    email_value = email_value
    sound_value = sound_value
    link_value = link_value

    if str(sound_value) == '0':
        play_default_sound()
    elif str(sound_value) == '1':
        webbrowser.open(link_value)

    response = messagebox.askokcancel(title="DSC ALARM", message="UTHHJAO")

    # send_mail will make it lazy, threading
    if str(email_value) == '1':
        fromaddr = "testroom960@gmail.com"
        toaddr = "kushchoudhary8@gmail.com"
        password_ = open('pass.txt', 'r')
        password = password_.readline()
        password_.close()

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = 'Its '+str(hour_value)+':'+str(min_value)+' now'
        data_c = {'Username': 'Kush'}
        data_r = str(data_c)
        body = data_r
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, password)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

    if response and str(sound_value) == '0':
        mixer.music.stop()

    if not response:
        try:
            mixer.music.stop()
        except:
            pass


def turn_off():
    pass


def start_alarm(hour_value, min_value, snooze_value,
                email_value, sound_value, link_value, on_off_value):
    hour_value = hour_value
    min_value = min_value
    snooze_value = snooze_value
    email_value = email_value
    sound_value = sound_value
    link_value = link_value

    now = dt.now()

    if str(now.hour) == str(hour_value) and str(now.minute) == str(min_value):
        alarm_ring(hour_value, min_value, snooze_value,
                   email_value, sound_value, link_value, on_off_value)
    else:
        root.after(100, activate)


def check_alarm(hour_value, min_value, snooze_value,
                email_value, sound_value, link_value, on_off_value):
    if on_off_value == 0:
        turn_off()
    else:
        start_alarm(hour_value, min_value, snooze_value,
                    email_value, sound_value, link_value, on_off_value)


def play_default_sound():
    mixer.init()
    mixer.music.load('alarm_tune.mp3')
    mixer.music.play()


def activate():
    hour_value = hour_variable.get()
    min_value = min_variable.get()
    snooze_value = snooze.get()
    email_value = email_int_var.get()
    sound_value = var.get()
    link_value = link_link.get()
    on_off_value = on_off_var.get()

    print(hour_value, min_value, snooze_value,
          email_value, sound_value, link_value, on_off_value)

    check_alarm(hour_value, min_value, snooze_value,
                email_value, sound_value, link_value, on_off_value)


root.geometry("470x150")
root.title("DSC ALARM")

on_off_var = IntVar()
on_button = Radiobutton(root, text="ON", variable=on_off_var,
                        value=1, activebackground='sky blue')
on_button.grid(row=0, column=0, padx=5, pady=5, ipadx=6)

off_button = Radiobutton(root, text="OFF", variable=on_off_var,
                         value=0, activebackground='firebrick1')
off_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

set_button = Button(
    root, text='SET', activebackground='gold', command=activate)
set_button.grid(row=0, column=2, padx=10, pady=5, ipadx=5)

time_label = Label(root, text='  TIME(H:M)')
time_label.grid(row=1, column=0, padx=4, pady=10)


hour_variable = Spinbox(root, from_=0, to=12, width=5, textvariable='HOUR')
hour_variable.grid(row=1, column=1, padx=5, pady=10)
min_variable = Spinbox(root, from_=0, to=60, width=5, textvariable='MIN')
min_variable.grid(row=1, column=2, padx=5, pady=10)

email_text = Label(root, text='MAIL ME')
email_text.grid(row=2, column=0, padx=4)
email_int_var = IntVar()
email_check = Checkbutton(
    root, selectcolor='sky blue', state=NORMAL, width=4, variable=email_int_var)
email_check.grid(row=2, column=1, padx=2, pady=5)

snooze = Scale(root, from_=0, to=15, orient=HORIZONTAL)
snooze.set(5)
snooze.grid(row=1, column=3)

sound_text = Label(root, text='SOUND  ')

sound_text.grid(row=3, column=0, padx=0)
var = IntVar()
default_button = Radiobutton(root, text="DEFAULT", variable=var, value=0)
default_button.grid(row=3, column=1, padx=1, pady=5)

link_button = Radiobutton(root, text="LINK", variable=var, value=1)
link_button.grid(row=3, column=2, padx=2, pady=5)

link_link = Entry(root, bg='azure', highlightcolor='cyan')
link_link.grid(row=3, column=3)


def time():
    string = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, time)


time_label = Label(root, font=('calibri', 20, 'bold'),
                   background='gold',
                   foreground='white')
time_label.grid(row=0, column=3)
time()


root.mainloop()
