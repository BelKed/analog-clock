import tkinter
import math
import time
from datetime import datetime

canvas_size = 700
canvas = tkinter.Canvas(bg="#091921", width=canvas_size, height=canvas_size)
canvas.pack()

radius = 250
angle = 270
digits = hour = minute = second_1 = second_2 = circle = 0


def calculate(_angle, _radius):
    x = math.cos(math.radians(_angle)) * _radius + canvas_size / 2
    y = math.sin(math.radians(_angle)) * _radius + canvas_size / 2

    return x, y


def line(_x, _y, _width, _color):
    return canvas.create_line(canvas_size / 2, canvas_size / 2, _x, _y, width=_width, fill=_color,
                              capstyle="round")


def draw():
    global digits, hour, minute, second_1, second_2, circle

    canvas.delete(digits, hour, minute, second_1, second_2, circle)

    tm = datetime.utcnow()
    epoch = time.mktime(tm.timetuple())
    tm += datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)

    digital_time = tm.strftime('%d.%m.%Y %H:%M:%S')
    digits = canvas.create_text(canvas_size / 2, 40, text=digital_time, fill="#5a5f72",
                                font=("JetBrains Mono", 25, "bold"))

    x, y = calculate(tm.hour * 30 + tm.minute / 2 - 90, radius - 110)
    hour = line(x, y, 12, "#53051e")

    x, y = calculate(tm.minute * 6 + tm.second / 10 - 90, radius - 60)
    minute = line(x, y, 7, "#777777")

    x, y = calculate(tm.second * 6 + tm.microsecond * 0.000006 - 90, radius - 35)
    second_1 = line(x, y, 4, "#0b5384")

    x, y = calculate(tm.second * 6 + tm.microsecond * 0.000006 + 90, radius - 210)
    second_2 = line(x, y, 4, "#0b5384")

    circle = canvas.create_oval(canvas_size / 2 - 10, canvas_size / 2 - 10, canvas_size / 2 + 10,
                                canvas_size / 2 + 10, fill="#002700", width=0)


for i in range(12):
    x, y = calculate(angle, radius)
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#181d2f", outline="#131725", width=3)

    number = i
    if number == 0: number = 12
    canvas.create_text(x, y, text=number, fill="#5a5f72", font=("JetBrains Mono", 17, "bold"))

    angle += 360 / 12

while True:
    draw()
    canvas.update()
