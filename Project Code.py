# Importing all the necessary modules

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk, filedialog
import pyttsx3
from PIL import ImageTk, Image
import speech_recognition as sr
import os

# Creating the python text to speech and speech to text functions

muted = False

def TTS():

    e = pyttsx3.init()
    def talk():
        def check_voice():
            if (gender == 'Male'):
                e.setProperty('voice', v[0].id)
                e.setProperty('volume', (volume_) / 100)
                e.say(text)
                e.runAndWait()
            else:
                e.setProperty('voice', v[1].id)
                e.setProperty('volume', (volume_) / 100)
                e.say(text)
                e.runAndWait()
        text = txt_area.get(1.0, END)
        gender = gender_combo.get()
        speed = speed_combo.get()
        volume_ = scale_level.get()
        v = e.getProperty('voices')
        if (text):
            if (speed == 'Fast'):
                e.setProperty('rate', 300)
                check_voice()
            elif (speed == 'Normal'):
                e.setProperty('rate', 150)
                check_voice()
            else:
                e.setProperty('rate', 50)
                check_voice()
    def download():
        def check_voice():
            if (gender == 'Male'):
                e.setProperty('voice', v[0].id)
                e.setProperty('volume', (volumes) / 100)
                path=filedialog.askdirectory()
                os.chdir(path)
                e.save_to_file(text,'outputmale.mp3')
                e.runAndWait()
            else:
                e.setProperty('voice', v[1].id)
                e.setProperty('volume', (volumes) / 100)
                path = filedialog.askdirectory()
                os.chdir(path)
                e.save_to_file(text, 'outputfemale.mp3')
                e.runAndWait()
    
        text=txt_area.get(1.0,END)
        gender=gender_combo.get()
        speed=speed_combo.get()
        volumes=scale_level.get()
        v=e.getProperty('voices')
        if(text):
            if(speed=='Fast'):
                e.setProperty('rate',300)
                check_voice()
            elif(speed=='Normal'):
                e.setProperty('rate',150)
                check_voice()
            else:
                e.setProperty('rate',50)
                check_voice()

    def mute():
        global muted
        ## Unmuting
        if muted:       
            e.setProperty('volume',0.7)
            volumeBtn.configure(image=volumePhoto)
            scale_level.set(70)
            muted = False
        else:
            ## Muting
            e.setProperty('volume',0)
            volumeBtn.configure(image=mutePhoto)
            scale_level.set(0)
            muted = True

    def back():
        root.destroy()
        
    
    root=Toplevel()
    root.geometry("700x500")
    root.title('Text to Speech Converter')
    root.iconbitmap("icon.ico")
    bg1 = ImageTk.PhotoImage(file = "1.jpg")

  
#Creating the canvas
    canvas2 = Canvas( root, width = 600, height = 400)
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, image = bg1, anchor = "nw")

#textbox
    f1=Frame(root,relief=GROOVE,bd=5)
    f1.place(x=15,y=70,width=670,height=200)

#scrollbar 
    scrol_bar=Scrollbar(f1,orient=VERTICAL)
    scrol_bar.pack(side=RIGHT,fill=Y)
    txt_area=Text(f1,font=('Tenorite',15,'bold'),bg='grey99',yscrollcommand=scrol_bar.set,wrap=WORD)
    txt_area.pack(fill=BOTH)
    scrol_bar.config(command=txt_area.yview)

#OPTIONS
    gender_lbl=Label(root,text='Voice',font='Tenorite 18 bold',width=10,bg='yellow',fg='red')
    gender_lbl.place(x=60,y=280)

    speed_lbl=Label(root,text='Speed',font='Tenorite 18 bold',width=10,bg='yellow',fg='red')
    speed_lbl.place(x=280,y=280)

    volume_lbl=Label(root,text='Volume',font='Tenorite 18 bold',width=10,bg='yellow',fg='red')
    volume_lbl.place(x=500,y=280)

#===================combo box====================
    gender_combo=ttk.Combobox(root,values=['Male','Female'],font='tenorite 10 bold',state='r',width=10)
    gender_combo.place(x=80,y=330)
    gender_combo.set('Male')

    speed_combo=ttk.Combobox(root,values=['Fast','Normal','Slow'],font='tenorite 10 bold',state='r',width=10)
    speed_combo.place(x=300,y=330)
    speed_combo.set('Fast')

    scale_level=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=130,font='tenorite 10 bold',width=10)
    scale_level.place(x=500,y=315)
    scale_level.set(100)

#===================buttons======================


    play_btn=Button(root,text='Play',font='tenorite 16 bold',width=10, bg='light green',activebackground='yellow',relief=RAISED,bd=5,command=talk)
    play_btn.place(x=60,y=380)

    pause_btn=Button(root,text='Pause',font='tenorite 16 bold',width=10,bg='light green',activebackground='yellow',relief=RAISED,bd=5)
    pause_btn.place(x=280,y=380)

    d_btn=Button(root,text='Save',width=10,font='tenorite 16 bold ',relief=RAISED,bg='light green',activebackground='yellow',bd=5,command=download)
    d_btn.place(x=500,y=380)

    volumePhoto = PhotoImage(file = 'volume.png')
    mutePhoto = PhotoImage(file = 'mute.png')
    volumeBtn = Button(root, image=volumePhoto, command=mute)
    volumeBtn.place(x=330, y=440)

    exit_btn =Button(root,text='EXIT',font='Tenorite 12 bold',bg='red',activebackground='yellow',relief=RAISED,bd=5,command=exit)
    exit_btn.place(x=625,y=450)

    back_btn =Button(root,text='Back',font='tenorite 12 bold',bg='red',activebackground='yellow',relief=RAISED,bd=5,command= back)
    back_btn.place(x=25, y=450)

#=========================

    slider_lebel=Label(root,bd=0)
    slider_lebel.place(x=700,y=100)

    root.configure(bg='CadetBlue1')
    root.mainloop()

def STT():

    r = sr.Recognizer()

    def record():
        with sr.Microphone() as source:
            audio_data = r.record(source, duration = 5)
            text = r.recognize_google(audio_data)
            return text
    
    def back():
        root.destroy()

    def note():
        note = '''
    This program is in its development stage !
    It may not provide accurate results and can give ERRORS!!.
    '''
        showinfo("Note", note)

#==================================Main STT Window===========================================

    root = Tk()
    root.title('Speech to Text Converter')
    root.geometry('500x350')
    root.resizable(0, 0)
    root.configure(bg='Cyan')

#===================================Title================================================= 

    lbl_title=Label(root,text="Speech to Text Converter",font='Tenorite 20 bold')
    lbl_title.place(x=0,y=0,relwidth=1)

#==================================Text Box=================================================

    text = Text(root, font=12, height=5, width=49,bd=5)
    text.place(x=25, y=70)


#==================================Button Placement=======================================



    record_btn = Button(root, text='Record', bg='Sienna',font='Tenorite 16 bold',relief=RAISED,bd=5, command=lambda: text.insert(END,record()))
    record_btn.place(x=210, y=220)

    exit_btn =Button(root,text='Exit',font='Tenorite 10 bold',bg='red',activebackground='yellow',relief=RAISED,bd=5,command=exit)
    exit_btn.place(x=445, y=300)

    back_btn =Button(root,text='Back',font='tenorite 10 bold',bg='red',activebackground='yellow',relief=RAISED,bd=5,command= back)
    back_btn.place(x=15, y=300)

    note_btn = Button(root, text='!! NOTE !!', font=('Tenorite bold',12), bg='yellow', relief = RAISED, bd=5, command=note)
    note_btn.place(x=213, y=300)

    root.update()
    root.mainloop()



#=========================================Opening Window======================================================

def main_window():    
    root = Tk()
    root.title('Python Text to Speech & Speech to Text Converter')
    root.geometry('600x400')
    root.resizable(0, 0)
    root.configure(bg='Cyan')


    bg = ImageTk.PhotoImage(file = "2.jpg")
    
    # Create Canvas
    canvas1 = Canvas( root, width = 400, height = 400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")

    def instruction():
        instructions = '''
    These are the instructions:
    1. Wait for some time because STT and TTS conversions take time.
    2. Pause for 5 seconds to end your phrase in STT conversion, because that is the current duration given.
    '''
        showinfo("Instructions before beginning", instructions)

    instruction_btn = Button(root, text='! Instructions before starting !', font=('Tenorite bold', 16), bg='MediumPurple', relief = RAISED, bd=5, command=instruction)
    instruction_btn.place(x=145, y=220)

    tts_btn =Button(root,text='Text to Speech',font='tenorite 18 bold',bg='light green',activebackground='yellow',relief=RAISED,bd=5,command =TTS)
    tts_btn.place(x=100, y=150)

    stt_btn =Button(root,text='Speech to Text',font='tenorite 18 bold',bg='light green',activebackground='yellow',relief=RAISED,bd=5,command = STT)
    stt_btn.place(x=300, y=150)

    exit_btn =Button(root,text='EXIT',font='tenorite 12 bold',bg='red',activebackground='yellow',relief=RAISED,bd=5,command=exit)
    exit_btn.place(x=270, y=300)


    root.update()
    root.mainloop()

main_window()