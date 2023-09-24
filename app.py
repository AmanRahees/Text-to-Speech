import os
import random
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import pyttsx3

app = Tk()
app.title("Text-to-Speech Convert App")
app.config(bg="#0278ab")
app.geometry("600x450")
app.resizable(False, False)
appIcon = ImageTk.PhotoImage(Image.open("icon.jpg"))
app.iconphoto(False, appIcon)

engine = pyttsx3.init()

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            textArea.delete('1.0', END)
            textArea.insert('1.0', content)

def convertTTS():
    try:
        text = textArea.get(1.0, END)
        voice = voice_box.get()
        speed = speed_box.get()
        pitch = pitch_box.get()
        voices = engine.getProperty('voices')

        def setVoice():
            if voice == "Male":
                engine.setProperty('voice', voices[0].id)
                engine.setProperty('pitch', 50 if pitch == "Low" else 200 if pitch == "High" else 100)
                engine.say(text)
                engine.runAndWait()
            else:
                engine.setProperty('voice', voices[1].id)
                engine.setProperty('pitch', 50 if pitch == "Low" else 200 if pitch == "High" else 100)
                engine.say(text)
                engine.runAndWait()
        if text:
            if speed == "Fast":
                engine.setProperty('rate', 250)
                setVoice()
            elif speed == "Normal":
                engine.setProperty('rate', 150)
                setVoice()
            else:
                engine.setProperty('rate', 60)
                setVoice()
            saveButton = Button(app, text="Save", compound=LEFT, image=saveIcon, command=download, width=80, bg="#ddd", font=("Poppins", 12)).place(x=500, y=400)
    except:
        print("An Error Occured")
        return

def download():
    try:
        text = textArea.get(1.0, END)
        voice = voice_box.get()
        speed = speed_box.get()
        pitch = pitch_box.get()
        voices = engine.getProperty('voices')
        filename = 'VOICE' + str(random.randint(1111111,9999999)) + ".mp3"
        def setVoice():
            if voice == "Male":
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            engine.setProperty('pitch', 50 if pitch == "Low" else 200 if pitch == "High" else 100)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, filename=filename)
            engine.runAndWait()
        if text:
            if speed == "Fast":
                engine.setProperty('rate', 250)
                setVoice()
            elif speed == "Normal":
                engine.setProperty('rate', 150)
                setVoice()
            else:
                engine.setProperty('rate', 60)
                setVoice()
            saveButton = Button(app, text="Save", compound=LEFT, image=saveIcon, width=80, bg="#ddd", font=("Poppins", 12)).place(x=500, y=400)
    except:
        print("An Error Occured!")
        

top_Frame = Frame(app, bg="#fff", width=600, height=80)
top_Frame.grid(row=0, column=0)
appLogo = ImageTk.PhotoImage(Image.open("logo.png"))
Label(top_Frame, image=appLogo, bg="White").place(x=20, y=20)
Label(top_Frame, text="TEXT TO SPEECH", font=("Poppins", 14, "bold"), bg='#fff').place(x=55, y=30)

textArea = Text(app, font=("Poppins", 12))
textArea.place(x=10, y=100, width=350, height=300)

loadButton = Button(app, text="Load File", padx=10, pady=3, command=load_file).place(x=10, y=410)
convertButton = Button(app, text="Convert", padx=10, pady=3, command=convertTTS).place(x=100, y=410)

Label(app, text="VOICE", bg="#0278ab", fg="#fff", font=("Poppins", 12)).place(x=390, y=100)
Label(app, text="SPEED", bg="#0278ab", fg="#fff", font=("Poppins", 12)).place(x=500, y=100)
Label(app, text="PITCH", bg="#0278ab", fg="#fff", font=("Poppins", 12)).place(x=390, y=180)

voice_box = Combobox(app, values=['Male', 'Female'], state='r', font=("Poppins", 12), width=8)
voice_box.place(x=370, y=130)
voice_box.set('Male')
speed_box = Combobox(app, values=['Slow', 'Normal', 'Fast'], state='r', font=("Poppins", 12), width=8)
speed_box.place(x=480, y=130)
speed_box.set('Normal')
pitch_box = Combobox(app, values=['Low', 'Normal', 'High'], state='r', font=("Poppins", 12), width=8)
pitch_box.place(x=370, y=210)
pitch_box.set('Normal')

saveIcon = ImageTk.PhotoImage(Image.open("save.png"))

app.mainloop()