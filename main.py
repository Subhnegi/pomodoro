
from time import time
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    Timer_label.config(text="Timer")
    check_marklabel.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_time=WORK_MIN*60
    short_break_time=SHORT_BREAK_MIN*60
    long_break_time=LONG_BREAK_MIN*60

    if reps%8==0:
        countdown(long_break_time)
        Timer_label.config(text="Break",fg=RED)
    elif reps%2==0:
        countdown(short_break_time)
        Timer_label.config(text="Break",fg=PINK)
    else:
        countdown(work_time)
        Timer_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes=math.floor(count/60)
    seconds=count%60
    if seconds<10:
        seconds=f"0{seconds}"
    if minutes<10:
        minutes=f"0{minutes}"
    
    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔"
        check_marklabel.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("POMODORO")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100, 130, text="00:00", font=(
    FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)


Timer_label = Label(fg=GREEN, text="Timer", font=(
    FONT_NAME, 40, "bold"), bg=YELLOW)
Timer_label.grid(row=0, column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2, column=0)


Reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
Reset_button.grid(row=2, column=2)

check_marklabel=Label(fg=GREEN,bg=YELLOW)
check_marklabel.grid(row=3,column=1)
window.mainloop()
