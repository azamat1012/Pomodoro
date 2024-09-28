from tkinter import *
import math
import os

# ------------------------CONSTANTS------------------------

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f5e0c1"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
timer_running = False  # Track whether the timer is running

# ------------------------TIMER RESET----------------------


def reset_timer():
    global reps
    global timer_running
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title_lable.config(text="Timer")
    check_mark.config(text="")
    reps = 0  # Reset repetitions
    timer_running = False  # Allow the timer to start again

# ------------------------TIMER MECHANISM------------------------


def start_timer():
    global reps
    global timer_running
    if not timer_running:  # Only start the timer if it's not running
        timer_running = True
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            title_lable.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_lable.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)
            title_lable.config(text="Work", fg=GREEN)


# ------------------------COUNTDOWN MECHANISM------------------------


img_dir = os.path.dirname(__file__)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check_mark.config(text=mark)


# ------------------------UI SETUP------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=50, bg=YELLOW)

title_lable = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 65, 'bold'), bg=YELLOW, highlightthickness=0)
title_lable.grid(column=2, row=1)

check_mark = Label(bg=YELLOW, fg='green', font=(FONT_NAME, 70))
check_mark.grid(column=2, row=3)

canvas = Canvas(width=500, height=390, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=f"{img_dir}/image.png")
canvas.create_image(250, 200, image=tomato_img)
timer_text = canvas.create_text(
    250, 200, text="25:00", fill='white', font=(FONT_NAME, 65, 'bold'))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()
