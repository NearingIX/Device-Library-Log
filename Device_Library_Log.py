# Device Library Log
import datetime

totalDevices = 0
allDevices = {}
# Append new devices to a txt log
deviceLibraryFile = open('Device_Library_Log.txt', 'a')

# Open log and read contents
def digestFile():
    deviceLibraryFile = open('Device_Library_Log.txt', 'r')
    readFile = deviceLibraryFile.read()
    print("~ Current Devices ~")
    print(readFile)

def addDevice():
    print("Welcome! How many devices would you like to add?")

    while True:
        try:
            global i
            numberOfDevices = input()
            deviceTotal = int(numberOfDevices)
            if deviceTotal <= 0:
                break
            elif deviceTotal >= 1:
                for i in range(deviceTotal):
                    global totalDevices
                    global allDevices
                    deviceNameKey = "Device Name"
                    deviceNameValue = input("Enter the device name:")
                    deviceTypeKey = "Device Type"
                    deviceTypeValue = input("Enter the type of the device:")
                    notesKey = "Notes:"
                    notesValue = input("Enter any notes:")
                    dateTimeStampKey = "Recorded on"
                    dateTimeStampValue = str(datetime.datetime.now())
                    device = {deviceNameKey:deviceNameValue, deviceTypeKey:deviceTypeValue, 
                    notesKey:notesValue, dateTimeStampKey:dateTimeStampValue}
                    allDevices.update(device)
                    # Writes each device to a new line
                    deviceLibraryFile.write(str(device) + "\n")
                    totalDevices += 1
                break
        except ValueError:
            print("Please enter an integer:")
            continue

digestFile()
addDevice()
deviceLibraryFile.close()
print("Thank you for using the Device Library Log.\nPlease press enter to quit.")
exitProgram = input()
