import fmtransmit
import RPi.GPIO

def writeFile(freq, freqHop, delay):
    f = open(r"flowVariables.txt","w")
    freqS = str(freq)+"\n"
    hopS = str(freqHop)+"\n"
    delayS = str(delay)+"\n"
    varList = [freqS, hopS, delayS]
    for L in varList:
        f.writelines(L)
    f.close()

def determineScript(isHopping, isIntermittent):
    if isHopping == "T":
        print("Executing frequency hopping flowgraph...")
    elif isIntermittent == "T":
        print("Executing intermittent flowgraph...")
    else:
        print("Continuous Flowgraph chosen")
        fmtransmit.main()

centerFreq = float(input("Enter the frequency for this transmission (Hz): "))
isHopping = input("Is the transmission frequency hopping? (T/F): ")
if isHopping == "T":
    hopFreq = float(input("What is the frequency hop for this transmission: "))
else:
    hopFreq = 0
isIntermittent = input("Is the transmission intermittent? (T/F): ")
if isIntermittent == "T":
    delay = float(input("What is the time delay for each transmission: "))
else:
    delay = 0
    
writeFile(centerFreq, hopFreq, delay)
determineScript(isHopping, isIntermittent)