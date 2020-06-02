from tkinter import *

global height_canvas, width_canvas, count
height_canvas = 600
width_canvas = 800
count = 0

def start(event):
    global height_canvas, width_canvas, count, lb
    count = 0
    lb["text"] = f"{count}"
    lb.place(x=400, y=10)
    ball.movement()
    bar.movement()

def game_over():
    global lb
    lb["text"] = "Você perdeu."
    lb.place(x=350, y=100)

class Bar:
    def __init__(self, canvas):
        self.acelX = 0
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, height_canvas-100, 200, height_canvas-90, fill="red")
        self.pos = self.canvas.coords(self.id)


        self.canvas.bind_all("<KeyPress-Left>", lambda k: self.move_left())
        self.canvas.bind_all("<KeyPress-Right>", lambda k: self.move_rigth())
        #self.movement()

    def movement(self):
        self.canvas.move(self.id, self.acelX, 0)

        self.pos = self.canvas.coords(self.id)
        #print(self.pos)
        if self.pos[0] <= 0 or self.pos[2] >= width_canvas:
            self.acelX = 0


        self.canvas.after(50, self.movement)
    def move_left(self):
        if self.pos[0] > 0:
            self.acelX = -10
        else:
            self.acelX = 0
    def move_rigth(self):
        if self.pos[2] < width_canvas:
            self.acelX = 10
        else:
            self.acelX = 0

class Ball:
    def __init__(self, canvas, bar):
        self.canvas = canvas
        self.bar = bar
        self.acelX = 8
        self.acelY = 8
        self.id = canvas.create_oval(0, 0, 15, 15, fill="green")


        #self.movement()

    def movement(self):
        self.canvas.move(self.id, self.acelX, self.acelY)
        self.pos = self.canvas.coords(self.id)
        # print(f"Pos: {self.pos}")

        if self.pos[0] <= 0:
            self.acelX = 8

        if self.pos[1] <= 0:
            self.acelY = 8

        if self.pos[2] >= width_canvas:
            self.acelX = -8

        #if self.pos[3] >= height_canvas:
         #   self.acelY = -10

        if bar.pos[0] <= self.pos[2] <= bar.pos[2] and (self.pos[3] >= bar.pos[1]):
            self.acelY = -8
            global count, lb
            count += 1
            lb["text"] = f"{count}"

        if self.pos[3] <= height_canvas:
            self.canvas.after(50, self.movement)
        else:
            game_over()



janela = Tk()

canvas = Canvas(janela, height=height_canvas, width=width_canvas)
#canvas.create_oval(0, 0, 15, 15, fill="green")
canvas.pack()

bar = Bar(canvas)
ball = Ball(canvas, bar)

lb = Label(canvas, text="Clique para iniciar o jogo")
lb.place(x=300, y=100)

canvas.bind_all("<Button-1>", start)

janela.mainloop()
