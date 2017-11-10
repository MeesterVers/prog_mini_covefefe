from tkinter import * #imports
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from main import *

root = Tk()     #creeer het hoofdscherm
root.geometry("1200x700")           #zet de grootte van de window
root.resizable(width=False, height=False)       #zorgt ervoor dat de grootte niet aangepast kan worden
root.title("Mini Project")
root.configure(background='white')
informatie_frame = Frame(master=root, bg='white')

def output_reis_informatie(reis_informatie_lijst):
    row = 0
    informatie_frame.pack(side=LEFT, padx=20,)

    vertrektijd = Label(master=informatie_frame, text="Tijd", font=('Helvetica', 14, 'bold'), bg='white')
    vertrektijd.grid(pady=30, padx=40, row=row, column=1)

    eindbestemming = Label(master=informatie_frame, text="Naar", font=('Helvetica', 14, 'bold'), bg='white')
    eindbestemming.grid(pady=30, padx=50, row=row, column=2, sticky=W)

    type_trein = Label(master=informatie_frame, text="Vervoerder", font=('Helvetica', 14, 'bold'), bg='white')
    type_trein.grid(pady=30, padx=50, row=row, column=3, sticky=W)

    spoor = Label(master=informatie_frame, text="Spoor", font=('Helvetica', 14, 'bold'), bg='white')
    spoor.grid(pady=30, padx=40, row=row, column=4, sticky=W)

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

def station_select(selected_station):
    user_station = stations_list_box.selection_get()
    request_status = "good"
    stations_list_box.pack_forget()
    welkom_lbl.pack_forget()
    meerdere_stations_lbl.pack_forget()
    reis_informatie_lijst = ander_vertrek_station(user_station, request_status) #get reis informatie alles is goed
    output_reis_informatie(reis_informatie_lijst)
# def station_select

def andere_station():
    mogelijke_stations_lijst = []
    user_station = station_textbox.get()
    user_station = user_station.title() #hoofdletters
    request_status = "bad"

    if user_station != "":
        mogelijke_stations_lijst = ander_vertrek_station(user_station, request_status)

        if len(mogelijke_stations_lijst) > 1:
            for station in mogelijke_stations_lijst:
                stations_list_box.insert(mogelijke_stations_lijst.index(station)+1, station)

            welkom_lbl['text'] = "Oops er zijn meerdere stations met de naam " + user_station
            meerdere_stations_lbl['text'] = "Kies aub 1 van de gegeven stations"
            meerdere_stations_lbl.pack()
            stations_list_box.pack()
            search_station_bttn.pack_forget()
            station_textbox.pack_forget()
            stations_list_box.bind('<<ListboxSelect>>', station_select)

        if len(mogelijke_stations_lijst) == 1:
            request_status = "good"
            search_station_bttn.pack_forget()
            station_textbox.pack_forget()
            reis_informatie_lijst = ander_vertrek_station(user_station, request_status) #get reis informatie alles is goed
            output_reis_informatie(reis_informatie_lijst)
    else:
        showinfo(title='Error', message="Oops u heeft geen station ingevuld")
# einde

def huidige_station():
    root.configure()
    label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    terug_bttn.pack()
    labelframe.pack()

    reis_informatie_lijst = hudige_vertrek_station()
    output_reis_informatie(reis_informatie_lijst)
# def huidge station

def ander_station_page():
    label.pack_forget()
    img.place_forget()
    buttonframe.pack_forget()
    terug_bttn.pack()
    welkom_lbl.pack()
    station_textbox.pack()
    search_station_bttn.pack(pady=10)
# def ander_station

def terug():
    img.place(x=0,y=0)
    label.pack()
    buttonframe.pack(side=LEFT)
    labelframe.pack_forget()
    terug_bttn.pack_forget()
    welkom_lbl.pack_forget()
    station_textbox.pack_forget()
    search_station_bttn.pack_forget()
    # remove_output_labels()
    informatie_frame.pack_forget()
#def terug 

def remove_output_labels():
    vertrektijd.grid_forget()
    eindbestemming.grid_forget()
    type_trein.grid_forget()
    spoor.grid_forget()
# remove output labels

BackgroundImage = Image.open('images/NS_GUI.png')
render1 = ImageTk.PhotoImage(BackgroundImage)
HuidigStationImage = Image.open('images/button_huidig-station.png')
render2 = ImageTk.PhotoImage(HuidigStationImage)
AnderStationImage = Image.open('images/button_ander-station.png')
render3 = ImageTk.PhotoImage(AnderStationImage)


img = Label(master=root, image=render1)
img.place(x=0,y=0)

label= Label(master=root,text='Reisinformatie Terminal', foreground='blue')
label.pack()


buttonframe = Frame(master=root, bg='#FDD037')
buttonframe.pack(side=LEFT)
button1 = Button(master=buttonframe, image=render2, command=huidige_station, bg='#FDD037')
button1.grid(row=0,column=0,padx=35, pady='10')
button2 = Button(master=buttonframe, image=render3,command=ander_station_page, bg='#FDD037')
button2.grid(row=1,column=0,padx=35, pady='10')
terug_bttn = Button(master=root, text='Terug',command=terug)

welkom_lbl = Label(master=root, text='Voer het station in vanaf waar U de vertrekinformatie wilt.', bg='white', fg='#01579B')
meerdere_stations_lbl = Label(bg='white', fg='#01579B')

stations_list_box = Listbox(root)
station_textbox = Entry(master=root)
search_station_bttn = Button(master=root, text='Haal informatie', command=andere_station) 
labelframe = Frame(master=root)
root.mainloop()