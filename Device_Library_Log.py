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

digestFile()

def addDevice():
    print("Welcome! How many devices would you like to add?")

    while True:
        try:
            numberOfDevices = input()
            deviceTotal = int(numberOfDevices)
            if deviceTotal <= 0:
                break
            elif deviceTotal >= 1:
                for i in range(deviceTotal):
                    global totalDevices
                    global allDevices
                    deviceTypeKey = input("Enter the type of device:")
                    deviceNameValue = input("Enter the device name:")
                    notesKey = "Notes:"
                    notesValue = input("Enter any notes:")
                    dateTimeStampKey = "Device Logged On: "
                    dateTimeStampValue = str(datetime.datetime.now())
                    device = {deviceTypeKey:deviceNameValue, notesKey:notesValue, dateTimeStampKey:dateTimeStampValue}
                    allDevices.update(device)
                    # Writes each device to a new line
                    deviceLibraryFile.write(str(device) + "\n")
                    totalDevices += 1
                break
        except ValueError:
            print("Please enter an integer:")
            continue

addDevice()
print("Thank you for using the Device Library Log.")
deviceLibraryFile.close()