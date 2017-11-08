from tkinter import * #imports
from PIL import Image, ImageTk
from main import *
root = Tk()     #creeer het hoofdscherm
root.geometry("1200x700")           #zet de grootte van de window
root.resizable(width=False, height=False)       #zorgt ervoor dat de grootte niet aangepast kan worden

def huidige_station():
    label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    labelframe.pack()
    button3.pack()
    hudige_vertrek_station()

def ander_station():
    label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    label5.pack()
    entry1.pack()
    button3.pack()

def clicked():
    label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    labelframe.pack()
    button3.pack()
def terug():
    img.place(x=0,y=0)
    label.pack()
    buttonframe.pack(side=LEFT)
    labelframe.pack_forget()
    button3.pack_forget()
    label5.pack_forget()
    entry1.pack_forget()

BackgroundImage = Image.open('NS_GUI.png')     # Opent de image
render1 = ImageTk.PhotoImage(BackgroundImage)
HuidigStationImage = Image.open('button_huidig-station.png')
render2 = ImageTk.PhotoImage(HuidigStationImage)
AnderStationImage = Image.open('button_ander-station.png')
render3 = ImageTk.PhotoImage(AnderStationImage)
#searchbuttonImage = Image.open('searchbutton.png')
#render4 = ImageTk.PhotoImage(searchbuttonImage)
#placeholder image voor searchbutton


img = Label(master=root, image=render1)
img.place(x=0,y=0)

label= Label(master=root,text='Reisinformatie Terminal',foreground='blue')
label.pack()


buttonframe = Frame(master=root)
buttonframe.pack(side=LEFT)
button1 = Button(master=buttonframe, image=render2, command=huidige_station)
button1.grid(row=0,column=0,padx=50)
button2 = Button(master=buttonframe, image=render3,command=ander_station)
button2.grid(row=1,column=0,padx=50)

button3 = Button(master=root, text='<',command=terug)

label5 = Label(master=root, text='Voer het station in vanaf waar U de vertrekinformatie wilt.',foreground='blue')
entry1 = Entry(master=root)
#searchbutton = Button(master=root,image=render4,command=TBD)

labelframe = Frame(master=root)
label1 = Label(master=labelframe,text='Intercity Maastricht, via s-Hertogenbosch, Eindhoven, Weert',background='white')
label2 = Label(master=labelframe,text='Intercity Rotterdam, via Gouda, Alexander',background='grey')
label3 = Label(master=labelframe,text='Sprinter Baarn, via Overvecht, Den Dolder, Soest',background='white')
label4 = Label(master=labelframe,text='Intercity Den Helder, via Amstel, Amsterdam C., Adam Sloterdijk',background='grey')
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)


root.mainloop()

for background in label1, label2, label3, label4:
    achtergrondkleur=2
    if achtergrondkleur%2==0:
        background='white'
        achtergrondkleur+1
    else:
        background='grey'
        achtergrondkleur+1