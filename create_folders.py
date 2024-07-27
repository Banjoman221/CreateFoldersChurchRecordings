#!/usr/bin/python3
from calendar import MONDAY, SUNDAY, day_abbr, month
import os
import sys
import calendar
from os import mkdir, makedirs
import datetime
import time
import customtkinter 

mainPath = os.getcwd()
allFiles = os.listdir(mainPath)
allFilesArrayFolders = []
allFilesArray = []

print(allFiles)

for x in allFiles:
    try:
        if int(x):
            allFilesArrayFolders.append(int(x))
    except ValueError:
        print('not a year folder')

if len(allFilesArrayFolders) == 0:
    theYear = datetime.datetime.now().strftime("%Y")
    print(theYear)
    allFilesArray.append(theYear)
    allFilesArrayMax = max(allFilesArray)

if len(allFilesArrayFolders) != 0:
    allFilesArrayMax = max(allFilesArrayFolders)

newFilesArray = []

for x in range(10):
    if len(allFilesArray) == 1:
        allFilesArrayNumber = int(allFilesArrayMax) + x
    else:
        allFilesArrayNumber = int(allFilesArrayMax) + 1 + x

    print(allFilesArrayNumber)
    newFilesArray.append(str(allFilesArrayNumber))

print(newFilesArray)

def year_input(input_year):
    while True:
        try:
            # Get the input for the year
            year = input(input_year)
            # Get the current date
            current_date = datetime.datetime.now()
            # Exit if year is equal "q"
            if year == "q":
                sys.exit()

            # Check to see if year is greater than or equal to current year and return year
            elif int(year) >= int(current_date.strftime("%Y")):
                return int(year)
                break
            else:
                print("That is not a valid year")
        # If year input is another value try again
        except ValueError:
            print("That is not a valid year")
            continue

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Create Folders")
        self.geometry("220x150+500+200")

        self.yearFrame = customtkinter.CTkFrame(self)
        self.yearFrame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsw")

       #self.yearLabel = customtkinter.CTkLabel(self.yearFrame, text="Enter Year: ")
       #self.yearLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.yearOptionMenu = customtkinter.CTkOptionMenu(self.yearFrame, values=newFilesArray);
        self.yearOptionMenu.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        self.yearButton = customtkinter.CTkButton(self, text="submit", command= lambda:self.createFolders(self.yearOptionMenu.get()))
        self.yearButton.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

    def createFolders(self, newYear):
        # Get the Year
        year = int(newYear)
        print(year)
        for y in newFilesArray:
            if y == newYear:
                newFilesArray.remove(y)

        newestYear = int(newYear) + 10
        newFilesArray.append(str(newestYear))
        self.yearOptionMenu.configure(values = newFilesArray)
        self.yearOptionMenu.set(newFilesArray[0])

        new_month = {}
        num_months = []

        for months in calendar.month_name:
            num_months.append(0)
            if months != "":
                new_month[len(num_months) - 1] = months

        print(new_month)
        # Set the first weekday to Sunday
        calendar.setfirstweekday(calendar.SUNDAY)

        # Creates the Folders by iterating through new_month dictionary
        for num, month in new_month.items():
            # Prints the Year and month to the console
            print("{}/{}-{}".format(year, num, month))

            """
            Gets the number of days for a given month and returns an array of numbers by week with 0 
            not being in the given month
            """
            matrix = calendar.monthcalendar(year, num)

            print(matrix)

            # Iterates through the array
            for x in matrix:
                # If the array index = 0 skip it
                if x[0] != 0:
                    makedirs(
                        "{}/{}-{}/{} {} {}".format(year,
                                                   num, month, month, x[0], "Sun AM")
                    )
                    makedirs(
                        "{}/{}-{}/{} {} {}".format(year,
                                                   num, month, month, x[0], "Sun PM")
                    )
                if x[3] != 0:
                    makedirs(
                        "{}/{}-{}/{} {} {}".format(year,
                                                   num, month, month, x[3], "Wed")
                    )

if __name__ == "__main__":
    app = App()
    app.mainloop()
