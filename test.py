from tkinter import * 
from tkinter.messagebox import showinfo
from main import *

def station_select(selected_station):
	user_station = stations_list_box.selection_get()
	request_status = "good"
	ander_vertrek_station(user_station, request_status)
	stations_list_box.pack_forget()
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
			meerdere_stations_lbl = Label(text="Kies aub 1 van de gegeven stations")
			meerdere_stations_lbl.pack()
			stations_list_box.pack()
			search_station_bttn.pack_forget()
			station_textbox.pack_forget()
			stations_list_box.bind('<<ListboxSelect>>', station_select)

		if len(mogelijke_stations_lijst) == 1:
			request_status = "good"
			ander_vertrek_station(user_station, request_status) #get reis informatie alles is goed
	else:
		showinfo(title='Error', message="Oops u heeft geen station ingevuld")
# einde

root = Tk() # Creëer het hoofdscherm 
stations_list_box = Listbox(root)
welkom_lbl = Label(text='Van welk station wilt u reis informatie weten?')
welkom_lbl.pack()

station_textbox = Entry(master=root) 
station_textbox.pack(padx=10, pady=10)

search_station_bttn = Button(master=root, text='Haal informatie', command=andere_station) 
search_station_bttn.pack(pady=10)
root.mainloop()