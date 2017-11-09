from tkinter import * #imports
from PIL import Image, ImageTk
from main import *

root = Tk()     #creeer het hoofdscherm
root.geometry("1200x700")           #zet de grootte van de window
root.resizable(width=False, height=False)       #zorgt ervoor dat de grootte niet aangepast kan worden
root.title("Mini Project")
root.configure(background='white')

def output_reis_informatie(reis_informatie_lijst):
    row = 0
    informatie_frame = Frame(master=root, bg='white')
    informatie_frame.pack(side=LEFT, padx=20,)

    vertrektijd = Label(master=informatie_frame, text="Tijd", font=('Helvetica', 14, 'bold'), bg='white')
    vertrektijd.grid(pady=30, padx=40, row=row, column=1)

    eindbestemming = Label(master=informatie_frame, text="Naar", font=('Helvetica', 14, 'bold'), bg='white')
    eindbestemming.grid(pady=30, padx=50, row=row, column=2, sticky=W)

    type_trein = Label(master=informatie_frame, text="Vervoerder", font=('Helvetica', 14, 'bold'), bg='white')
    type_trein.grid(pady=30, padx=50, row=row, column=3, sticky=W)

    spoor = Label(master=informatie_frame, text="Spoor", font=('Helvetica', 14, 'bold'), bg='white')
    spoor.grid(pady=30, padx=40, row=row, column=4, sticky=W)

    button3.pack()

    for reis_informatie in reis_informatie_lijst:
        row = row + 1

        vertrektijd = Label(master=informatie_frame, text=reis_informatie[0] + '\n' + reis_informatie[5], font=('Helvetica', 12), bg='white', fg='#01579B')
        vertrektijd.grid(pady=5, padx=40, row=row, column=1)

        eindbestemming = Label(master=informatie_frame, text=reis_informatie[3] + '\n' + reis_informatie[4] + '\n' + reis_informatie[6] + '\n' + reis_informatie[7], font=('Helvetica', 12), bg='white')
        eindbestemming.grid(pady=5, padx=50, row=row, column=2, sticky=W)

        type_trein = Label(master=informatie_frame, text=reis_informatie[2], font=('Helvetica', 12), bg='white')
        type_trein.grid(pady=5, padx=50, row=row, column=3, sticky=W)

        spoor = Label(master=informatie_frame, text=reis_informatie[1], font=('Helvetica', 12), bg='white')
        spoor.grid(pady=10, padx=40, row=row, column=4)
# def print_reis_informatie

def huidige_station():
    root.configure()
    label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    labelframe.pack()

    reis_informatie_lijst = hudige_vertrek_station()
    output_reis_informatie(reis_informatie_lijst)
# def huidge station

def ander_station():
    label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    label5.pack()
    entry1.pack()
    button3.pack()
# def ander_station

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

label= Label(master=root,text='Reisinformatie Terminal', foreground='blue')
label.pack()


buttonframe = Frame(master=root, bg='#FDD037')
buttonframe.pack(side=LEFT)
button1 = Button(master=buttonframe, image=render2, command=huidige_station, bg='#FDD037')
button1.grid(row=0,column=0,padx=35, pady='10')
button2 = Button(master=buttonframe, image=render3,command=ander_station, bg='#FDD037')
button2.grid(row=1,column=0,padx=35, pady='10')
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