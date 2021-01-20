from tkinter import *
from tkinter.font import Font
from Backend import *


class GUI:
    def __init__(self,master):
        mainFont = Font(size=13)
        defaultBg = "#242424"
        defaultFg = "#ffffff"

        master.title("Salah Time App")
        master.configure(bg="#242424")

        InputFrame=Frame(master)
        InputFrame.configure(bg=defaultBg)
        InputFrame.pack(padx=50, pady=50)

        DateFrame=Frame(master)
        DateFrame.configure(bg=defaultBg)
        DateFrame.pack(padx=10, pady=10)

        DisplayFrame=Frame(master)
        DisplayFrame.config(bg=defaultBg)
        DisplayFrame.pack(padx=10, pady=10)



        # CREATING WIDGETS
        # entry Labels
        countryOrCityList=["Country","City"]
        i=0
        for j in range(2):
            label=Label(InputFrame,text=f"{countryOrCityList[j]}", font=mainFont, bg=defaultBg, fg=defaultFg)
            label.grid(row=i, column=0)
            i=+1

        # entry fields
        self.CountryEntry=Entry(InputFrame, width=15, font=mainFont)
        self.CityEntry=Entry(InputFrame,width=15, font=mainFont)


        # buttons
        self.searchButton=Button(InputFrame,
                                 text="search",
                                 width=22,
                                 font=mainFont,
                                 borderwidth=0,
                                 command=lambda: self.connect(DisplayFrame,
                                                              DateFrame,
                                                              font=mainFont,
                                                              bg=defaultBg,
                                                              fg=defaultFg))

        # DISPLAYING WIDGETS
        # entry fields
        self.CountryEntry.grid(row=0, column=1, pady=2)
        self.CityEntry.grid(row=1, column=1, pady=2)

        # buttons
        self.searchButton.grid(row=2, column=0, pady=2, columnspan=2)


    def connect(self, timingsFrame,datesFrame, font, fg, bg):
        country=self.CountryEntry.get()
        city=self.CityEntry.get()

        #===== salah timings ========#
        salahList=getSalahTimes(country,city)
        i=0
        for j in range(len(salahList)):
            TimingsLabel=Label(timingsFrame, text=f"{salahList[j]}", font=font, fg=fg, bg=bg)
            TimingsLabel.grid(row=i, column=0)
            i+=1

        #===== dates timings ========#
        datesList=createDateList(country,city)
        k=0
        for l in range(len(datesList)):
            DateLabel=Label(datesFrame,text=f"{datesList[l]}", font=font, fg=fg, bg=bg)
            DateLabel.grid(row=k, column=0)
            k+=1



root=Tk()
gui=GUI(root)
root.mainloop()