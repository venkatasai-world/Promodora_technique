from tkinter import *
from tkinter import messagebox
import time
import math

reps = 0
box = Tk()

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        messagebox.showinfo("Work", "Work Session Started!")
        count_down(work_sec)
    elif reps % 8 != 0:
        messagebox.showinfo("Break", "Time for a short break!")
        count_down(short_break_sec)
    else:
        messagebox.showinfo("Break", "Time for a long break!")
        count_down(long_break_sec)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        box.after(1000, count_down, count - 1)
    else:
        start_timer()

def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")

box.title("Pomodoro")
box.config(padx=100, pady=50, bg="#f7f5dd")

box_title = Label(box, text="Timer", font=("Arial", 35, "bold"), bg="#f7f5dd", fg="#9bdeac")

canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold"))

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", bg="#f7f5dd", fg="#9bdeac")
check_mark.grid(column=1, row=3)

box_title.grid(column=1, row=0)
canvas.grid(column=1, row=1)

box.mainloop()
