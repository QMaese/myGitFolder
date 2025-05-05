import tkinter as tk
import os
## import final_skeletal_code.py as fsc

## Function that waters plant
def waterPlant():
    plant = setDisp.get()
    if plant in plantWaterCounts:
        plantWaterCounts[plant] += 1
        timesLabel.config(text=f"Times Watered: {plantWaterCounts[plant]}")
        print(f"Watered {plant}!")
    else:
        print("Please select a plant first.")
    ## fsc.water_plant()
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


#### MAIN PROGRAM ####

## Main Window
root = tk.Tk()
root.title("Plant Watering System")
root.geometry("300x330")
root.configure(bg="light green")

## Project Title Label
titleLabel = tk.Label(root, text="Plant Watering System",\
                      font=('Arial', 20),bg="light green")
titleLabel.pack(pady=20, expand=True, fill='both')

## Manual Water Button
waterButton     = tk.Button(root, text="Water Plant", command=waterPlant,\
                        font=('Arial', 14), bg="#ffffff",\
                            fg="#444444", padx=20, pady=10)
waterButton.pack(pady=20, expand=True, fill='both')

## Times Manually Watered Label
timesWatered = 0
timesLabel   = tk.Label(root, text=f"Times Watered: {timesWatered}",\
                        font=('Arial',14), bg="light green")
timesLabel.pack(pady=5, expand=True, fill='both')

## Dropdown Menu
setDisp        = tk.StringVar()
setDisp.set('Select Plant')
displayOptions = ['Select Plant']
dropDown       = tk.OptionMenu(root, setDisp, *displayOptions)
dropDown.config(font=('Arial',14))
dropDown.pack(pady=5, expand=True, fill='both')
plantWaterCounts = {}
loadData()

## Plant Entry Label
plantEntryLabel = tk.Label(root, text="Enter new plant name:",\
                           font=('Arial',14), bg="light green")
plantEntryLabel.pack(pady=5, expand=True, fill='both')

## Frame
newPlantFrame = tk.Frame(root, bg='light green')
newPlantFrame.pack(expand=True, fill='both')

## Plant Entry Button
plantEntry      = tk.Entry(newPlantFrame, font=('Arial',14))
plantEntry.pack(side=tk.LEFT, padx=5, expand=True, fill='both')

## Add Plant Button
addPlantButton = tk.Button(newPlantFrame, text='Add Plant', command=addPlant,\
                           font=('Arial',14), bg='#ffffff', fg='#444444',\
                           padx=20, pady=10)
addPlantButton.pack(side=tk.LEFT, padx=5, expand=True, fill='both')

## Saves on Exit
def onClose():
    saveData()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", onClose)    

root.mainloop()
