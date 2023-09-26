import tkinter as tk
from tkinter import ttk
from tkinter import *
import fmtransmit

interface = tk.Tk()
interface.title("Threat Emitter Interface")

interface_width = 6000
interface_height = 400

screen_width = interface.winfo_screenwidth()
screen_height = interface.winfo_screenheight()

center_x = int((screen_width / 2) - (interface_width / 2))
center_y = int((screen_height / 2) - (interface_height / 2))

geometry = "{}x{}+{}+{}".format(interface_width, interface_height, center_x, center_y)
interface.geometry(geometry)

#defaults
f = 0.0
h = False
d = False

#GUI Functions
def clickedSDR():
    print("Sent to SDR")
    file = open(r"guiVariables.txt","w")
    freqString = str(float(f.get()))+"\n"
    hopString = str(isHopping.get())+"\n"
    delayString = str(isDelay.get())+"\n"
    variableList = [freqString, hopString, delayString]
    for L in variableList:
        file.writelines(L)
    file.close()
    print(freqString)
    print(hopString)
    print(delayString)
    if isHopping.get() == True:
        print("freq hoppng")
        #Frequency Hopping flowgraph gets called here
    else:
        fmtransmit.main()
    #Write variables to a file
    #GNU flowgraph then reads the file to execute

def setFrequency():
    print(f.get())

def setHopping():
    print("Frequency Hopping selected")
    print(isHopping.get())

def setDelay():
    print("Time Delay selected")
    print(isHopping.get())
 
#####

#GUI Variables
userFreq = tk.StringVar()
isHopping = tk.BooleanVar()
isDelay = tk.BooleanVar()
#####

sendSDRButton = ttk.Button(interface, text="Send to SDR", command=clickedSDR)
sendSDRButton.pack()

enterFreqButton = ttk.Label(interface, text="Enter the Frequency in Hz")
enterFreqButton.pack()
f = ttk.Entry(interface)
f.pack()
sendFreqButton = ttk.Button(interface, text="Save Frequency", command = setFrequency)
sendFreqButton.pack()

hoppingOption = ttk.Checkbutton(interface, text="Frequency Hopping",command=setHopping,variable=isHopping)
hoppingOption.pack()

delayOption = ttk.Checkbutton(interface, text="Time Delayed Transmission",command=setDelay,variable=isDelay)
delayOption.pack()

interface.mainloop()

