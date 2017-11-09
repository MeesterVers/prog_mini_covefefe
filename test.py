from tkinter import * 
from main import *

def huidige_station():
	reis_informatie_lijst = hudige_vertrek_station()
	for reis_informatie in reis_informatie_lijst:
		label = Label(text=reis_informatie[3])
		label.pack()
# einde

root = Tk() # Creëer het hoofdscherm 
label = Label(text='Hello World')
label.pack()

button = Button(master=root, text='Druk hier', command=huidige_station) 
button.pack(pady=10)
root.mainloop()