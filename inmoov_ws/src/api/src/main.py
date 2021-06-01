from json_generator import JSON_generator

import roslaunch

import Tkinter as tk
import ttk

control_json = JSON_generator("../control/inmoov_control.json")
control_json.reset()
control_json.save_json()

def open_hand():
    control_dict = {
        "robot/arm/left/hand/finger/middle/servo/angle": 100,
        "robot/arm/left/hand/finger/little/servo/angle": 50,
        "robot/arm/left/hand/finger/pointer/servo/angle": 100,
        "robot/arm/left/hand/finger/thumb/servo/angle": 100,
        "robot/arm/left/hand/finger/ring/servo/angle": 50,
    }
    control_json.change_values(control_dict)
    control_json.save_json()

def close_hand():
    control_dict = {
        "robot/arm/left/hand/finger/middle/servo/angle": 50,
        "robot/arm/left/hand/finger/little/servo/angle": 100,
        "robot/arm/left/hand/finger/pointer/servo/angle": 50,
        "robot/arm/left/hand/finger/thumb/servo/angle": 50,
        "robot/arm/left/hand/finger/ring/servo/angle": 100,
    }
    control_json.change_values(control_dict)
    control_json.save_json()

#write the new window function which
#will be called when button pressed
def demo_window():
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)

    window.geometry('600x600')
    b1 = tk.Button(window, text ="Open hand", command = open_hand)
    b2 = tk.Button(window, text ="Close hand", command = close_hand)

    b1.pack()
    b2.pack()
    canvas.pack()

def manual_window():
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)

    window.geometry('1000x100')
    # Label
    ttk.Label(window, text = "Thumb", 
            font = ("Arial", 10)).grid(column = 0, 
            row = 15, padx = 10, pady = 5)
    
    ttk.Label(window, text = "Index", 
            font = ("Arial", 10)).grid(column = 1, 
            row = 15, padx = 10, pady = 5)

    ttk.Label(window, text = "Middle", 
            font = ("Arial", 10)).grid(column = 2, 
            row = 15, padx = 10, pady = 5)

    ttk.Label(window, text = "Ring", 
            font = ("Arial", 10)).grid(column = 3, 
            row = 15, padx = 10, pady = 5)

    ttk.Label(window, text = "Pinky", 
            font = ("Arial", 10)).grid(column = 4, 
            row = 15, padx = 10, pady = 5)

    ttk.Label(window, text = "Mouth", 
            font = ("Arial", 10)).grid(column = 5, 
            row = 15, padx = 10, pady = 5)
    
    ttk.Label(window, text = "Eye right", 
            font = ("Arial", 10)).grid(column = 6, 
            row = 15, padx = 10, pady = 5)

    ttk.Label(window, text = "Eye left", 
            font = ("Arial", 10)).grid(column = 7, 
            row = 15, padx = 10, pady = 5)

    ttk.Label(window, text = "Neck translation", 
            font = ("Arial", 10)).grid(column = 8, 
            row = 15, padx = 10, pady = 5)

    ttk.Label(window, text = "Neck rotation", 
            font = ("Arial", 10)).grid(column = 9, 
            row = 15, padx = 10, pady = 5)

    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 0, 
            row = 16, padx = 10, pady = 5)
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 1, 
            row = 16, padx = 10, pady = 5 )
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 2, 
            row = 16, padx = 10, pady = 5 )
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 3, 
            row = 16, padx = 10, pady = 5 )
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 4, 
            row = 16, padx = 10, pady = 5 )
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 5, 
            row = 16, padx = 10, pady = 5)
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 6, 
            row = 16, padx = 10, pady = 5 )
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 7, 
            row = 16, padx = 10, pady = 5 )
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 8, 
            row = 16, padx = 10, pady = 5 )
    ttk.Entry(window, width =10,textvariable="0",
            font = ("Arial", 10)).grid(column = 9, 
            row = 16, padx = 10, pady = 5 )

    ttk.Button(window, width =10, text="Valider").grid(column = 9, 
            row = 16, padx = 10, pady = 5 )
    canvas.pack()

HEIGHT = 600
WIDTH = 600
#create original window (title not need but why not?)
root = tk.Tk()
root.title("new window making machine: ")
canvas = tk.Canvas(root, height=100, width=300)
canvas.pack()
#create button that will be placed
button1 = tk.Button(root, text="Demo",
                   command=lambda: demo_window())
button1.place(x=500, y=100)
button2 = tk.Button(root, text="Manual",
                   command=lambda: manual_window())
button2.place(x=100, y=100)
#can use .grid() or .place() instead of pack .place()
#is the best according to me if you want the most control of positions
button1.pack()
button2.pack()
root.mainloop()





#def __main__():
    

