# Alien by Dc117 Corp.
# Controls:
# O=Open eye
# L=Close eye
# WASD: Move eye
# Right Click: Burp

from tkinter import*
window=Tk()
window.title('Alien V1.00')
c=Canvas(window, height=300, width=400)
c.pack()
body=c.create_oval(100, 150, 300, 250, fill='green')
eye=c.create_oval(170, 70, 230, 130, fill='white')
eyeball=c.create_oval(190, 90, 210, 110, fill='black')
mouth=c.create_oval(150, 220, 250, 240, fill='red')
neck=c.create_line(200, 150, 200, 130)
hat=c.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')
def mouth_open():
    c.itemconfig(mouth, fill='black')
def mouth_close():
    c.itemconfig(mouth, fill='red')
words=c.create_text(200, 280, text='I am an alien!')
def steal_hat():
    c.itemconfig(hat, state=HIDDEN)
    c.itemconfig(words, text='Give my hat back!')
window.attributes('-topmost', 1)
def burp(event):
    mouth_open()
    c.itemconfig(words, text='Burp!')
c.bind_all('<Button-1>', burp)
def blink():
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)
def unblink():
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)
def blink2(event):
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)
def unblink2(event):
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)
c.bind_all('<KeyPress-o>', blink2)
c.bind_all('<KeyPress-l>', unblink2)
def eye_control(event):
    key=event.keysym
    if key=="w":
        c.move(eyeball, 0, -1)
    elif key=="s":
        c.move(eyeball, 0, 1)
    elif key=="a":
        c.move(eyeball, -1, 0)
    elif key=="d":
        c.move(eyeball, 1, 0)
c.bind_all('<Key>', eye_control)