from tkinter import *
from random import randint

global canvas_width, canvas_height, ball
canvas_width = 800
canvas_height = 600
ball = [0]


def without_isolation():
    print("without_isolation")
    global ball, canvas
    clear_canvas()
    create_balls()
    for i in range(1, len(ball)):
        ball[i].acelX = randint(1, 5)
        ball[i].acelY = randint(1, 5)

def weak_isolation():
    print("weak_isolation")
    global ball, canvas
    clear_canvas()
    create_balls()
    for i in range(1, len(ball), 2):
        ball[i].acelX = randint(1, 5)
        ball[i].acelY = randint(1, 5)

def isolation():
    print("isolation")
    global ball, canvas
    clear_canvas()
    create_balls()

    ball[20].acelX = randint(1, 5)
    ball[20].acelY = randint(1, 5)

def create_balls():
    global ball
    for x in range(1, canvas_width, 100):
        for y in range(1, canvas_height, 100):
            ball.append(Ball(canvas, [x, x + 15], [y, y + 15]))

def clear_canvas():
    global canvas, without_isolation_bt, weak_isolation_bt, isolation_bt
    without_isolation_bt.place_forget()
    weak_isolation_bt.place_forget()
    isolation_bt.place_forget()


class Ball:
    def __init__(self, canvas, posx, posy):
        self.canvas = canvas
        self.id = canvas.create_oval(posx[0], posy[0], posx[1], posy[1], fill="#D4D2D2")
        self.acelX = 0
        self.acelY = 0

        self.movement()
        self.collision()

    def movement(self):
        global canvas_height, canvas_width, ball
        self.canvas.move(self.id, self.acelX, self.acelY)
        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.acelX = 5+randint(0, 2)

        if self.pos[1] <= 0:
            self.acelY = 5+randint(0, 2)

        if self.pos[2] >= canvas_width:
            self.acelX = -5+randint(0, 2)

        if self.pos[3] >= canvas_height:
            self.acelY = -5+randint(0, 2)


        self.canvas.after(60, self.movement)

    def collision(self):
        global ball
        col = self.canvas.find_overlapping(self.pos[0], self.pos[1], self.pos[2], self.pos[3])
        if len(col) >= 2:
            for i in col:
                if ball[i].acelX == 0 and randint(0, 10) == 1:
                    ball[i].acelX = randint(1, 5)
                    ball[i].acelY = randint(1, 5)
                else:
                    ball[i].acelX = ball[i].acelX * (-1)
                    ball[i].acelY = ball[i].acelY * (-1)
                self.canvas.itemconfig(ball[i].id, fill="#C70E2A")
        self.canvas.after(60, self.collision)

global canvas
janela = Tk()
janela.title("Simulação Contágio")

canvas = Canvas(janela, width=canvas_width, height=canvas_height)
canvas.pack()

global without_isolation_bt, weak_isolation_bt, isolation_bt
without_isolation_bt = Button(canvas, width=20, text="Sem Isolamento", command=without_isolation)
without_isolation_bt.place(x=300, y=230)

weak_isolation_bt = Button(canvas, width=20, text="Isolamento Fraco", command=weak_isolation)
weak_isolation_bt.place(x=300, y=280)

isolation_bt = Button(canvas, width=20, text="Com Isolamento", command=isolation)
isolation_bt.place(x=300, y=330)


janela.mainloop()
