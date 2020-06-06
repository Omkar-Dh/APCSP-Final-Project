import os
import zipfile
from selenium import webdriver
import webbrowser
import time
from tkinter import *
from tkinter import messagebox

basicPath = os.path.expanduser('~')  # C:\Users\name

flag = True

flag2 = True

zipNeeded = False

unZipNeeded = False

numClass = 0

gpa = 0

mp1 = []

mp2 = []

mp3 = []

mp4 = []

classes = []

averages = []

gradeValuation = []

qualityPoints = []

downloads = os.path.join(basicPath, 'Downloads')  # C:\Users\name\Downloads

zippedPath = downloads + "\chromedriver_win32.zip"  # C:\Users\name\Downloads\chromedriver_win32.zip

unZippedPath = downloads + "\chromedriver"  # C:\Users\name\Downloads\chromedriver

browserPath = (unZippedPath + "\chromedriver.exe")  # C:\Users\name\Downloads\chromedriver.exe


def unZipFolder(zippedFile, destination):
    with zipfile.ZipFile(zippedFile, 'r') as zip_ref:
        zip_ref.extractall(destination)


def messageBox(message):
    root = Tk()

    root.withdraw()

    messagebox.showinfo("showinfo", message)


def setClasses(classNumber):
    for i in range(12):
        try:
            classes.append(browser.find_element_by_css_selector("#content > div.content-inner.ng-scope > div > "
                                                                "div.row.sortable.ng-scope > div > div > "
                                                                "div.box-content "
                                                                "> div:nth-child(2) > div:nth-child(1) > table > "
                                                                "tbody > "
                                                                "tr:nth-child(" + str(
                i) + ") > td:nth-child(1) > div > "
                     "strong").text)
            classNumber += 1

        except:
            pass


def setMP1(numberOfClasses):
    for i in range(numberOfClasses):
        mp1.append(browser.find_element_by_css_selector("#content > div.content-inner.ng-scope > div > "
                                                        "div.row.sortable.ng-scope > div > div > div.box-content > "
                                                        "div:nth-child(2) > div:nth-child(1) > table > tbody > "
                                                        "tr:nth-child(" + str(
            i + 1) + ") > td:nth-child(2) > p > a").text)

        if mp1[i] == '':
            mp1[i] = "000"


def setMP2(numberOfClasses):
    for i in range(numberOfClasses):
        mp2.append(browser.find_element_by_css_selector("#content > div.content-inner.ng-scope > div > "
                                                        "div.row.sortable.ng-scope > div > div > div.box-content > "
                                                        "div:nth-child(2) > div:nth-child(1) > table > tbody > "
                                                        "tr:nth-child(" + str(
            i + 1) + ") > td:nth-child(3) > p > a").text)

        if mp2[i] == '':
            mp2[i] = "000"


def setMP3(numberOfClasses):
    for i in range(numberOfClasses):
        mp3.append(browser.find_element_by_css_selector("#content > div.content-inner.ng-scope > div > "
                                                        "div.row.sortable.ng-scope > div > div > div.box-content > "
                                                        "div:nth-child(2) > div:nth-child(1) > table > tbody > "
                                                        "tr:nth-child(" + str(
            i + 1) + ") > td:nth-child(4) > p > a").text)
        if mp3[i] == '':
            mp3[i] = "000"


def setMP4(numberOfClasses):
    for i in range(numberOfClasses):
        mp4.append(browser.find_element_by_css_selector("#content > div.content-inner.ng-scope > div > "
                                                        "div.row.sortable.ng-scope > div > div > div.box-content > "
                                                        "div:nth-child(2) > div:nth-child(1) > table > tbody > "
                                                        "tr:nth-child(" + str(
            i + 1) + ") > td:nth-child(5) > p > a").text)
        if mp4[i] == '':
            mp4[i] = "000"


def stringToDoubleList(array):
    arr = [float(num_str) for num_str in array]
    return arr


def isWeighted(className):
    returnValue = False

    if "AP" in className:
        returnValue = True
    elif "Honor" in className or "Anatomy" in className or "Unified" in className or "Java" in className or " H " in className or "Calculus" in className:
        returnValue = True
    else:
        returnValue = False

    if "Pre-Calculus" in className:
        returnValue = False

    return returnValue


def gradeValue(grade):
    value = ""
    if grade >= 93:
        value = 4.0
    elif grade >= 90:
        value = 3.67
    elif grade >= 87:
        value = 3.33
    elif grade >= 83:
        value = 3.0
    elif grade >= 80:
        value = 2.67
    elif grade >= 77:
        value = 2.33
    elif grade >= 73:
        value = 2.0
    elif grade >= 70:
        value = 1.67
    elif grade >= 67:
        value = 1.33
    elif grade >= 63:
        value = 1.0
    elif grade >= 60:
        value = 0.67
    else:
        value = 0.0
    return value


if not (os.path.exists(unZippedPath)):
    while not (os.path.exists(zippedPath)):
        if flag:
            if not (os.path.exists(zippedPath)):
                print(" Could not find Zipped chrome driver folder \n Downloading new folder...")
                webbrowser.open('https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip')
                time.sleep(2)
                flag = False
                zipNeeded = True
        else:
            print("Waiting for Download...")

    print("Found Zipped Chrome Driver Folder")

while not (os.path.exists(unZippedPath)):
    if flag2:
        unZipFolder(zippedPath, unZippedPath)
        flag2 = False
        unZipNeeded = True
    else:
        print("Unzipping Folder")

if unZipNeeded:
    print("Folder Unzipped")

print("Finished Chrome Driver Installation ")

browser = webdriver.Chrome(browserPath)

browser.get("https://www.oncourseconnect.com/sso/index/wayne")

messageBox("Please Login to Oncourse to continue")

while not (browser.current_url == "https://www.oncourseconnect.com/#/dashboard"):
    time.sleep(2.5)
    print("Waiting for Login...")

print("Found Login Session\n\n")
browser.set_window_size(1100, 1100)

time.sleep(2)

setClasses(numClass)

numClass = len(classes)

setMP1(numClass)
setMP2(numClass)
setMP3(numClass)
setMP4(numClass)

print("CLASSES: ")
for i in range(numClass):
    print(classes[i] + "\n")

print("MP1: " + str(mp1) + "\n")
print("MP2: " + str(mp2) + "\n")
print("MP3: " + str(mp3) + "\n")
print("MP4: " + str(mp4) + "\n")

for i in range(numClass):
    a = mp1[i].split()
    mp1[i] = a[0]

for i in range(numClass):
    b = mp2[i].split()
    mp2[i] = b[0]

for i in range(numClass):
    c = mp3[i].split()
    mp3[i] = c[0]

for i in range(numClass):
    d = mp4[i].split()
    mp4[i] = d[0]

mp1 = stringToDoubleList(mp1)
mp2 = stringToDoubleList(mp2)
mp3 = stringToDoubleList(mp3)
mp4 = stringToDoubleList(mp4)

for i in range(numClass):
    if mp1[i] == 000 and mp2[i] == 000 and mp3[i] == 000:
        averages.append(mp4[i])
    elif mp2[i] == 000 and mp3[i] == 000 and mp4[i] == 000:
        averages.append(mp1[i])
    elif mp1[i] == 000 and mp3[i] == 000 and mp4[i] == 000:
        averages.append(mp2[i])
    elif mp2[i] == 000 and mp2[i] == 000 and mp4[i] == 000:
        averages.append(mp3[i])
    else:
        if mp1[i] == 000:
            averages.append(round(((mp2[i] + mp3[i] + mp4[i]) / 3.0), 2))
        elif mp2[i] == 000:
            averages.append(round(((mp1[i] + mp3[i] + mp4[i]) / 3.0), 2))
        elif mp3[i] == 000:
            averages.append(round(((mp1[i] + mp2[i] + mp4[i]) / 3.0), 2))
        elif mp4[i] == 000:
            averages.append(round(((mp1[i] + mp2[i] + mp3[i]) / 3.0), 2))
        else:
            averages.append(round(((mp1[i] + mp2[i] + mp3[i] + mp4[i]) / 4.0), 2))

print("Averages:" + str(averages))

for i in range(numClass):
    if isWeighted(classes[i]):
        classes[i] = 'weighted'

for i in range(numClass):
    if classes[i] == 'weighted':
        gradeValuation.append((gradeValue(averages[i]) + 1.0))
    else:
        gradeValuation.append(gradeValue(averages[i]))

for i in range(numClass):
    qualityPoints.append(gradeValuation[i] * 5)

sum = sum(qualityPoints)

sum -= gradeValuation[3] * 5

gpa = round((sum / ((numClass - 1) * 5)), 2)

print("\n Current Year GPA: " + str(gpa))
