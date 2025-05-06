import tkinter as tk
import tkinter.font as tkFont
import os
<<<<<<< HEAD
import Final_skeletal_code as fsc
import threading
import board
import RPi.GPIO as GPIO
import time

RED_LED=17
GREEN_LED=27
RELAY_PIN=23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(GREEN_LED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(RELAY_PIN, GPIO.OUT, initial = GPIO.LOW)
=======

>>>>>>> 1261e02690c5d8d528a67e9207628e93b9abaf9a
## Function that waters plant
def waterPlant():
    plant = setDisp.get()
    if plant in plantWaterCounts:
        plantWaterCounts[plant] += 1
        timesLabel.config(text=f"Times Watered: {plantWaterCounts[plant]}")
        print(f"Watered {plant}!")
    else:
        print("Please select a plant first.")
<<<<<<< HEAD
    fsc.water_plant()
=======
    ### Water pump functionality ###
>>>>>>> 1261e02690c5d8d528a67e9207628e93b9abaf9a
    ### Recieve input from soil moisture sensor ###

## Function that adds plant to the database
def addPlant():
    plant = plantEntry.get().strip()
    global plantWaterCounts
    if plant:
        if plant not in plantWaterCounts.keys():
            print('Plant Added!')
            displayOptions.append(plant)
            plantWaterCounts[plant] = 0
            menu = dropDown['menu']
            menu.add_command(label=plant,\
                             command=lambda value=plant: whenSelected(value)
                             )

## Function that changes label when a new plant is selected                           command=lambda value=plant: whenSelected(value))
def whenSelected(plant):
    setDisp.set(plant)
    count = plantWaterCounts.get(plant, 0)
    timesLabel.config(text=f'Times Watered: {count}')

## Function that saves data
def saveData():
    with open("plants.txt", "w") as file:
        for plant, count in plantWaterCounts.items():
            file.write(f"{plant},{count}\n")
    print("Data saved to plants.txt")

## Function that loads data
def loadData():
    if os.path.exists("plants.txt"):
        with open("plants.txt", "r") as file:
            for line in file:
                if ',' in line:
                    plant, count = line.strip().split(',', 1)
                    displayOptions.append(plant)
                    plantWaterCounts[plant] = int(count)
                    dropDown['menu'].add_command(
                        label=plant,
                        command=lambda value=plant: whenSelected(value))

<<<<<<< HEAD
thread = threading.Thread(target = fsc.check, daemon = True)
thread.start()
=======
>>>>>>> 1261e02690c5d8d528a67e9207628e93b9abaf9a

#### MAIN PROGRAM ####

## Main Window
root = tk.Tk()
root.title("Plant Watering System")
root.geometry("300x330")
root.configure(bg="light green")

## Project Title Label
titleFont  = tkFont.Font(family='Arial', size=16)
titleLabel = tk.Label(root, text="Plant Watering System", font=titleFont,\
                      bg="light green")
titleLabel.pack(pady=20, expand=True, fill='both')

## Manual Water Button
waterButtonFont = tkFont.Font(family='Arial', size=14)
waterButton     = tk.Button(root, text="Water Plant", command=waterPlant,\
                        font=waterButtonFont, bg="#ffffff", fg="#444444",\
                        padx=20, pady=10)
waterButton.pack(pady=20, expand=True, fill='both')

## Times Manually Watered Label
timesWatered = 0
timesFont    = tkFont.Font(family='Arial', size=14)
timesLabel   = tk.Label(root, text=f"Times Watered: {timesWatered}",\
                        font=timesFont, bg="light green")
timesLabel.pack(pady=5, expand=True, fill='both')

## Dropdown Menu
setDisp        = tk.StringVar()
setDisp.set('Select Plant')
displayOptions = ['Select Plant']
dropDownFont   = tkFont.Font(family='Arial', size=14)
dropDown       = tk.OptionMenu(root, setDisp, *displayOptions)
dropDown.config(font=dropDownFont)
dropDown.pack(pady=5, expand=True, fill='both')
plantWaterCounts = {}
loadData()

## Plant Entry Label
entryLabelFont  = tkFont.Font(family='Arial', size=14)
plantEntryLabel = tk.Label(root, text="Enter new plant name:",\
                           font=entryLabelFont, bg="light green")
plantEntryLabel.pack(pady=5, expand=True, fill='both')

## Frame
newPlantFrame = tk.Frame(root, bg='light green')
newPlantFrame.pack(expand=True, fill='both')

## Plant Entry Button
entryButtonFont = tkFont.Font(family='Arial', size=14)
plantEntry      = tk.Entry(newPlantFrame, font=entryButtonFont)
plantEntry.pack(side=tk.LEFT, padx=5, expand=True, fill='both')

## Add Plant Button
addPlantFont   = tkFont.Font(family='Arial', size=14)
addPlantButton = tk.Button(newPlantFrame, text='Add Plant', command=addPlant,\
                           font=addPlantFont, bg='#ffffff', fg='#444444',\
                           padx=20, pady=10)
addPlantButton.pack(side=tk.LEFT, padx=5, expand=True, fill='both')

## Saves on Exit
def onClose():
    saveData()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", onClose)

## Function that changes font size
def resize_fonts(event):
    newSize = max(8, int(event.width / 25))
    titleFont.configure(size=newSize)
    waterButtonFont.configure(size=newSize)
    timesFont.configure(size=newSize)
    dropDownFont.configure(size=newSize)
    entryLabelFont.configure(size=newSize)
    entryButtonFont.configure(size=newSize)
    addPlantFont.configure(size=newSize)
    

root.bind("<Configure>", resize_fonts)

<<<<<<< HEAD


=======
>>>>>>> 1261e02690c5d8d528a67e9207628e93b9abaf9a
root.mainloop()
