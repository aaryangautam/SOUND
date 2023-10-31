import tkinter as tk
from tkinter import ttk
from tkinter import *
#import fmtransmit
import wifitransmit

interface = tk.Tk()
interface.title("SOUND")


#STyle
bg_color = '#012866'

interface.configure(bg=bg_color)


interface_width = 600
interface_height = 400

screen_width = interface.winfo_screenwidth()
screen_height = interface.winfo_screenheight()

center_x = int((screen_width / 2) - (interface_width / 2))
center_y = int((screen_height / 2) - (interface_height / 2))

geometry = "{}x{}+{}+{}".format(interface_width, interface_height, center_x, center_y)
interface.geometry(geometry)

#defaults
f = 0.0
message ="None"
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
#THE SIGNAL WE WILL BE WORKING WITH
SIGNAL_CHOSEN = "FM/AM"

def change_signal(signal):
    SIGNAL_CHOSEN = signal
    menuButton.config(text=f"Choosen signal: {SIGNAL_CHOSEN}")
    
# Dropdown menu options 
menuButton = Menubutton(interface, text = "Choose signal")
menuButton.menu = Menu(menuButton)
menuButton['menu']=menuButton.menu
menuButton.menu.add_command(label='Bluetooth', command=lambda:change_signal("Bluetooth"))
menuButton.menu.add_command(label='Wi-Fi', command=lambda:change_signal("Wi-Fi"))
menuButton.menu.add_command(label='FM/AM', command=lambda:change_signal("FM/AM"))

menuButton.pack()


#sendSDRButton = Button(interface, text="Send to SDR",bg='white', command=clickedSDR)
#sendSDRButton.pack()

enterFreqButton = Label(interface, text="Enter the Frequency in Hz",bg=bg_color,fg='white')
enterFreqButton.pack()
f = ttk.Entry(interface)
f.pack()
sendFreqButton = Button(interface, text="Save Frequency",bg='white', command = setFrequency)
sendFreqButton.pack()

enterMessageButton = Label(interface, text="Choose message to send:",bg=bg_color,fg='white')
enterMessageButton.pack()
message = ttk.Entry(interface)
message.pack()
sendMessageButton = Button(interface, text="Save Message",bg='white', command = setFrequency)#change the command...
sendMessageButton.pack()


delayOption = Checkbutton(interface, text="Time Delayed Transmission",bg='white',command=setDelay,variable=isDelay)
delayOption.pack()


def start_transmission():
    wifitransmit.wifitransmit()
    print("sending wifi right now:::")

sendSDRButton = Button(interface, text="Send to SDR",bg='white', command=start_transmission())
sendSDRButton.pack()

sendSDRButton = Button(interface, text="STOP sending",bg='white', command=start_transmission())
sendSDRButton.pack
# if SIGNAL_CHOSEN == "Wi-Fi":
#     sendSDRButton = Button(interface, text="Send to SDR",bg='white', command=start_transmission())
#     sendSDRButton.pack()

#     sendSDRButton = Button(interface, text="STOP sending",bg='white', command=start_transmission())
#     sendSDRButton.pack
# else:
#     sendSDRButton = Button(interface, text="Send to SDR",bg='white', command=clickedSDR)
#     sendSDRButton.pack()

#     sendSDRButton = Button(interface, text="STOP sending",bg='white', command=clickedSDR)
#     sendSDRButton.pack()

interface.mainloop()

