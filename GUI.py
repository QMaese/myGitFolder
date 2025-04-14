import tkinter as tk

def waterPlant():
    print("Watering the plant!")
    global timesWatered
    timesWatered += 1
    timesLabel.config(text=f"Times Watered: {timesWatered}")

## Main Window
root = tk.Tk()
root.title("Plant Watering System")
root.geometry("300x200")
root.configure(bg="light green")  # light green background

## Project Title Label
titleLabel = tk.Label(root, text="Plant Watering System", font=("Arial", 16), bg="light green")
titleLabel.pack(pady=20)

## Manual Water Button
waterButton = tk.Button(root, text="Water Plant", command=waterPlant, font=("Arial", 14), bg="#ffffff", fg="#444444", padx=20, pady=10)
waterButton.pack(pady=20)

## Times Manually Watered Label
timesWatered = 0
timesLabel   = tk.Label(root, text=f"Times Watered: {timesWatered}", font=("Arial"), bg="light green")
timesLabel.pack(pady=5)

root.mainloop()
