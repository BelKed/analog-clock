import tkinter, math, time

width, height = 600, 700
canvas = tkinter.Canvas(bg="blue", width=width, height=height)
canvas.pack()

radius = 250
angle = 270
digits = second = minute = hour = 0


def calculate(_angle, _radius):
    x = math.cos(math.radians(_angle)) * _radius + width / 2
    y = math.sin(math.radians(_angle)) * _radius + height / 2

    return x, y


def draw():
    global digits, second, minute, hour

    canvas.delete(digits, second, minute, hour)
    tm = time.localtime()

    digital_time = f"{tm[2]:02}.{tm[1]:02}.{tm[0]:04} {tm[3]:02}:{tm[4]:02}:{tm[5]:02}"
    digits = canvas.create_text(300, 25, text=digital_time, fill="red", font="Arial 30")

    x, y = calculate(tm[5] * 6 - 90, radius - 30)
    second = canvas.create_line(width / 2, height / 2, x, y, fill="red", width=2)

    x, y = calculate(tm[4] * 6 - 90, radius - 50)
    minute = canvas.create_line(width / 2, height / 2, x, y, fill="green", width=3)

    x, y = calculate(tm[3] * 30 - 90, radius - 100)
    hour = canvas.create_line(width / 2, height / 2, x, y, fill="white", width=4)


for i in range(12):
    x, y = calculate(angle, radius)

    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="yellow", width=2)

    number = i
    if number == 0: number = 12
    canvas.create_text(x, y, text=number, fill="red", font="Arial 20")
    angle += 360 / 12

while True:
    draw()
    canvas.update()
