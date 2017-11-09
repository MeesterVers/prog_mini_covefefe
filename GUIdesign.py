from tkinter import * #imports
from PIL import Image, ImageTk
from main import *
root = Tk()     #creeer het hoofdscherm
root.geometry("1200x700")           #zet de grootte van de window
root.resizable(width=False, height=False)       #zorgt ervoor dat de grootte niet aangepast kan worden

def huidige_station():
    row = 0
    # label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    labelframe.pack()

    button3.pack()

    vertrektijd = Label(master=labelframe, text="Vertrek tijd", font=('Helvetica', 16, 'bold'))
    vertrektijd.grid(pady=10, row=row, column=1)

    spoor = Label(master=labelframe, text="Spoor", font=('Helvetica', 16, 'bold'))
    spoor.grid(pady=10, row=row, column=2)

    type_trein = Label(master=labelframe, text="Type trein", font=('Helvetica', 16, 'bold'))
    type_trein.grid(pady=10, row=row, column=2)

    eindbestemming = Label(master=labelframe, text="Eind bestemming", font=('Helvetica', 16, 'bold'))
    eindbestemming.grid(pady=10, row=row, column=3)

    tussen_stops = Label(master=labelframe, text="Tussen stops", font=('Helvetica', 16, 'bold'))
    tussen_stops.grid(pady=10, row=row, column=4)

    vertraging = Label(master=labelframe, text="Vertraging", font=('Helvetica', 16, 'bold'))
    vertraging.grid(pady=10, row=row, column=5)

    reis_advies = Label(master=labelframe, text="Tips", font=('Helvetica', 16, 'bold'))
    reis_advies.grid(pady=10, row=row, column=6)

    opmerking = Label(master=labelframe, text="Opmerkingen", font=('Helvetica', 16, 'bold'))
    opmerking.grid(pady=10, row=row, column=7)

    reis_informatie_lijst = hudige_vertrek_station()
    for reis_informatie in reis_informatie_lijst:
        row = row + 1 
        vertrektijd = Label(master=labelframe, text=reis_informatie[0], font=('Helvetica', 16))
        vertrektijd.grid(pady=10, row=row, column=1)

        spoor = Label(master=labelframe, text=reis_informatie[1], font=('Helvetica', 16))
        spoor.grid(pady=10, row=row, column=2)

        type_trein = Label(master=labelframe, text=reis_informatie[2], font=('Helvetica', 16))
        type_trein.grid(pady=10, row=row, column=2)

        eindbestemming = Label(master=labelframe, text=reis_informatie[3], font=('Helvetica', 16))
        eindbestemming.grid(pady=10, row=row, column=3)

        tussen_stops = Label(master=labelframe, text=reis_informatie[4], font=('Helvetica', 16))
        tussen_stops.grid(pady=10, row=row, column=4)

        vertraging = Label(master=labelframe, text=reis_informatie[5], font=('Helvetica', 16))
        vertraging.grid(pady=10, row=row, column=5)

        reis_advies = Label(master=labelframe, text=reis_informatie[6], font=('Helvetica', 16))
        reis_advies.grid(pady=10, row=row, column=6)

        opmerking = Label(master=labelframe, text=reis_informatie[7], font=('Helvetica', 16))
        opmerking.grid(pady=10, row=row, column=7)
# def huidge station

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

BackgroundImage = Image.open('images/NS_GUI.png')     # Opent de image
render1 = ImageTk.PhotoImage(BackgroundImage)
HuidigStationImage = Image.open('images/button_huidig-station.png')
render2 = ImageTk.PhotoImage(HuidigStationImage)
AnderStationImage = Image.open('images/button_ander-station.png')
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
button3 = Button(master=root, text='Terug',command=terug)

label5 = Label(master=root, text='Voer het station in vanaf waar U de vertrekinformatie wilt.',foreground='blue')
entry1 = Entry(master=root)
#searchbutton = Button(master=root,image=render4,command=TBD)

labelframe = Frame(master=root)
# label1 = Label(master=labelframe,text='Intercity Maastricht, via s-Hertogenbosch, Eindhoven, Weert',background='white')
# label2 = Label(master=labelframe,text='Intercity Rotterdam, via Gouda, Alexander',background='grey')
# label3 = Label(master=labelframe,text='Sprinter Baarn, via Overvecht, Den Dolder, Soest',background='white')
# label4 = Label(master=labelframe,text='Intercity Den Helder, via Amstel, Amsterdam C., Adam Sloterdijk',background='grey')
# label1.grid(row=0,column=0)
# label2.grid(row=1,column=0)
# label3.grid(row=2,column=0)
# label4.grid(row=3,column=0)


root.mainloop()

# for background in label:
#     achtergrondkleur=2
#     if achtergrondkleur%2==0:
#         background='white'
#         achtergrondkleur+1
#     else:
#         background='grey'
#         achtergrondkleur+1