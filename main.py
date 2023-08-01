from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("410x600+100-100")
root.title("Screen Recorder")
root.config(bg="#bcbfbf")
root.resizable(False,False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+".mp4"), 5)

def pause_rec():
    rec.pause_recording()

def stop_rec():
    rec.stop_recording()

def resume_rec():
    rec.resume_recording()

rec = pyscreenrec.ScreenRecorder()

# Icon on window title
image_icon = PhotoImage(file="images\icon.png")
root.iconphoto(False,image_icon)

# Background images
image1 = PhotoImage(file="images\white.png")
Label(root, image = image1, bg="#bcbfbf").place(x=2,y=35)

image2 = PhotoImage(file="images\black.png")
Label(root, image = image2, bg="#bcbfbf").place(x=160, y=200)

# Title and centre image
Lbl = Label(root, text="Screen Recorder", bg="#bcbfbf", font="Astonpoliz 15 bold" )
Lbl.pack(pady=20)

image3 = PhotoImage(file="images\recording.png")
Label(root, image = image3, bg="#bcbfbf").pack(pady=30)

# Entry for the filename to store the recording
Filename = StringVar()
entry = Entry(root, textvariable= Filename, width= 20, font= "Calibri 13")
entry.place(x=110, y=365)
Filename.set("recording")

# Buttons
image4 = PhotoImage(file="images\play_button.png")
play = Button(root,image = image4, bd = 0, bg = "#bcbfbf", command= start_rec)
play.place(x=65, y=410)

image5 = PhotoImage(file="images\pause_button.png")
pause = Button(root,image = image5, bd = 0, bg = "#bcbfbf", command= pause_rec)
pause.place(x=165, y=410)

resume = Button(root, text="resume", font="Calibri 13", bd = 0, width=8, height=1, command= resume_rec)
resume.place(x=160, y=500)

image6 = PhotoImage(file="images\stop_button.png")
stop = Button(root,image = image6, bd = 0, bg = "#bcbfbf", command= stop_rec)
stop.place(x=265, y=410)

root.mainloop()