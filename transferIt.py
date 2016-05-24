import shutil
import os

dwnld_Folder = "C:\\Users\\Juan Antonio\\Downloads\\" #My Downloads Folder
music_Folder = "C:\\Users\\Juan Antonio\\Music\\Unorganized\\"
usb_folder = "Q:\\APyTest"

alreadyExists = " is already present :/"
wasMoved = " has been moved :)"

def getDownloads(myDownloads):
    files = os.listdir(myDownloads)
    mp3files = []
    for file in files:
        if file.endswith(".mp3"):
            song = myDownloads+file
            mp3files.append((file,song))
    return (mp3files)

def moveToMusic(mp3List, myMusic):
    print ("==========================================")
    print ("MyMusic transfer initiated")
    print ("==========================================")

    musicFiles = os.listdir(myMusic)
    for mp3 in mp3List:
        if mp3[0] not in musicFiles:
            shutil.copy2(mp3[1],myMusic)
        #     print (mp3[0] + wasMoved)
        # else:
        #     print (mp3[0] + alreadyExists)

    print ("==========================================")
    print ("MyMusic transfer COMPLETED")
    print ("==========================================")
    return  (0)

def moveToUSB(mp3List, myUsb):
    print ("==========================================")
    print ("USB transfer initiated")
    print ("==========================================")

    usbFiles = os.listdir(myUsb)
    for mp3 in mp3List:
        if mp3[0] not in usbFiles:
            shutil.move(mp3[1],myUsb)
        #     print (mp3[0] + wasMoved)
        # else:
        #     print (mp3[0] + alreadyExists)

    print ("==========================================")
    print ("USB transfer COMPLETED")
    print ("==========================================")
    return (0)

def evaluateTransfer(songs):
    if len(songs) == 0:
        print ("=====================")
        print ("No MP3s to transfer!")
        print ("=====================")
    else:
        moveToMusic(songs, music_Folder)
        moveToUSB(songs, usb_folder)
    return

if __name__ == '__main__':
    songList = getDownloads(dwnld_Folder)
    evaluateTransfer(songList)
