from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#
count_down(5)

# Image - Using Canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Label - Timer
lbl_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
lbl_timer.grid(row=0, column=1)

# Button - Start
btn_start = Button(text="Start", highlightthickness=0)
btn_start.grid(row=2, column=0)

# Button - Reset
btn_reset = Button(text="Reset", highlightthickness=0)
btn_reset.grid(row=2, column=2)

# Label - Task
lbl_tracker = Label(text=CHECKMARK, fg=GREEN, bg=YELLOW)
lbl_tracker.grid(row=3, column=1)

window.mainloop()
