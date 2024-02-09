from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    canvas.itemconfig(timer_text, text='00:00:00')
    window.after_cancel(timer)
    timer_up.config(text='Timer')
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def caller():
    global reps
    reps += 1

    if reps % 8 == 0:
        to_do = LONG_BREAK_MIN
        timer_up.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        to_do = SHORT_BREAK_MIN
        timer_up.config(text="BREAK", fg=PINK)
    else:
        to_do = WORK_MIN
        timer_up.config(text="WORK", fg=GREEN)
    # hour = 0.001
    # to_do = hour * 60
    timer_up.config(text="TEST")
    down(count=to_do * 60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def down(count):
    count_hour = int(int(count / 60) / 60)
    count_min = int(count / 60) % 60
    count_sec = int(count % 60)
    if count_hour < 10:
        count_hour = f'0{count_hour}'
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_hour}:{count_min}:{count_sec}")

    # secs = mins % 60
    if count > 0:
        global timer
        timer = window.after(1000, down, count - 1)
    else:
        caller()
        mark = ""
        for i in range(int(reps/2)):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(pady=50, padx=100, bg=YELLOW)



timer_up = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_up.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=caller)
start_button.grid(column=0, row=2)

check_label = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_label.grid(column=1, row=3)



 
window.mainloop()