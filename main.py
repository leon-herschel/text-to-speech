from tkinter import *
from gtts import gTTS
from pygame import mixer
import time

root = Tk()
root.geometry("350x250")
root.resizable(0, 0)
root.configure(bg='white')
root.title('Text to Speech')

Label(root, text='TEXT TO SPEECH', font='roboto 20 bold', bg='white').pack()

Label(root, text='ENTER TEXT', font='roboto 15 bold', bg='white').place(x=20, y=60)

msg = StringVar()
input_box = Entry(root, textvariable=msg, width='50')
input_box.place(x=20, y=100)


def text_to_speech():
    message = input_box.get()
    speech = gTTS(text=message)
    filename = f"Speech_{int(time.time())}.mp3"
    speech.save(filename)
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()


def close():
    root.destroy()


def clear():
    input_box.delete(0, 'end')


Button(root, text='PLAY', font='roboto 15 bold', command=text_to_speech).place(x=25, y=135)
Button(root, text='EXIT', font='roboto 15 bold', command=close).place(x=100, y=135)
Button(root, text='CLEAR', font='roboto 15 bold', command=clear).place(x=170, y=135)

root.mainloop()
