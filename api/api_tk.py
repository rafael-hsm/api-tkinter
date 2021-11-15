from tkinter import *
import requests
import json


# http://www.omdbapi.com/?i=tt3896198&apikey=3ddfaf6c
class MovieData:

    def __init__(self):  # inicializamos as variáveis
        self.window = Tk()  # criamos janela básica
        self.window.title("Movie Data")  # título para a janela
        self.window.geometry("680x480+300+150")  # definimos tamanho e localização
        self.window.resizable(0, 0)  # informamos que ela não é escalonável

        self.frame = Frame(self.window)
        self.frame.pack()

        self.text_entry = Entry(self.frame, font="arial 16", width=30)
        self.text_entry.grid(row=0, column=0)

        self.button_search = Button(self.frame, text="Search", font='arial 13',
                                    command=self.search_button)
        self.button_search.grid(row=0, column=1)

        self.list = Listbox(self.window)
        self.list.pack(fill=BOTH, expand=YES)

        self.window.mainloop()

    def search_button(self):
        try:
            request = requests.get("http://www.omdbapi.com/?t=" + self.text_entry.get() + "&apikey=3ddfaf6c")
            dict = json.loads(request.text)

            self.list.delete(0, END)
            self.list.insert(END, ("Title: " + dict["Title"]))
            self.list.insert(END, ("Year: " + dict["Year"]))
            self.list.insert(END, ("Released: " + dict["Released"]))
            self.list.insert(END, ("Time: " + dict["Time"]))
            self.list.insert(END, ("Genre: " + dict["Genre"]))
            self.list.insert(END, ("Director: " + dict["Director"]))
        except:
            self.list.delete(0, END)
            self.list.insert(END, "Movie not found!")


MovieData()
