# Import necessary libraries
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import customtkinter as ctk
import os
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

def login():

    driver.get("https://appeears.earthdatacloud.nasa.gov/task/area")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))

    # Inputs username and password

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()


def tkinterCall():
    root = ctk.CTk()
    userText = tk.StringVar()
    passText = tk.StringVar()
    monthStartText = tk.StringVar()
    monthEndText= tk.StringVar()
    yearCountText = tk.StringVar()
    yearStartText = tk.StringVar()
    delayText = tk.StringVar()

    root.geometry("600x500")
    root.title("AppEEARS")
    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("dark")

    userLabel = ctk.CTkLabel(root,text="Username:")
    usernameBox = ctk.CTkEntry(root,font=("arial", 12),textvariable=userText)
    userLabel.grid(row=0,column=0,padx=0,pady=10)
    usernameBox.grid(row=0,column=1)

    passLabel = ctk.CTkLabel(root,text="Password:")
    passwordBox = ctk.CTkEntry(root,font=("arial", 12),textvariable=passText,show="*")
    passLabel.grid(row=1,column=0,padx=0,pady=10)
    passwordBox.grid(row=1,column=1)

    monthStartLabel = ctk.CTkLabel(root,text="Start Month:")
    monthStartBox = ctk.CTkEntry(root,font=("arial", 12),textvariable=monthStartText)
    monthStartLabel.grid(row=2,column=0,padx=100,pady=10)
    monthStartBox.grid(row=2,column=1)

    monthEndLabel = ctk.CTkLabel(root,text="End Month:")
    monthEndBox = ctk.CTkEntry(root,font=("arial", 12),textvariable=monthEndText)
    monthEndLabel.grid(row=3,column=0,padx=0,pady=10)
    monthEndBox.grid(row=3,column=1)

    yearStartLabel = ctk.CTkLabel(root,text="Start Year:")
    yearStartBox = ctk.CTkEntry(root,font=("arial", 12),textvariable=yearStartText)
    yearStartLabel.grid(row=4,column=0,padx=0,pady=10)
    yearStartBox.grid(row=4,column=1)

    yearCountLabel = ctk.CTkLabel(root,text="Year Count:")
    yearCountBox = ctk.CTkEntry(root,font=("arial", 12),textvariable=yearCountText)
    yearCountLabel.grid(row=5,column=0,padx=0,pady=10)
    yearCountBox.grid(row=5,column=1)

    delayLabel = ctk.CTkLabel(root,text="Delay: (start with 15)")
    delayBox = ctk.CTkEntry(root,font=("arial", 12),textvariable=delayText)
    delayLabel.grid(row=6,column=0,padx=0,pady=10)
    delayBox.grid(row=6,column=1)

    button = ctk.CTkButton(root, text = "Go!",command=lambda: getTextFields(usernameBox,passwordBox,monthStartBox,monthEndBox,yearCountBox,yearStartBox,delayBox,root))
    button.grid(row=9,column=1)
    root.mainloop()
# !!!!!!! CHANGE TO USERNAME/PASSWORD TO APPEARS !!!!!!!
def getTextFields(user,passw,start, end,years,yearStart,delayNum,root):
    global username
    global password
    global startMonth
    global endMonth
    global startYear
    global yearCount
    global delay

    username = user.get()
    password = passw.get()
    startMonth = int(start.get())
    endMonth = int(end.get())
    startYear = int(yearStart.get())
    yearCount = int(years.get())
    delay = int(delayNum.get())
    login()
    root.destroy()




def checkLeap(year):
    if(year % 4 == 0):
        return True
    return False

tkinterCall()

months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Open a chrome window that links to the APPEARS website
#login()

#driver.quit()
#tkinterCall()
# Starts a new request
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, ("//img[@class='thumbnail ng-star-inserted']"))))
button = driver.find_element(By.XPATH, ("//img[@class='thumbnail ng-star-inserted']"))
button.click()
time.sleep(2)

# Path to shapefile
working_directory = os.getcwd()
file_path = working_directory + "Shapefile.zip"
shapefile_path = "Shapefile.zip"
shapefile_path = os.path.join(working_directory,shapefile_path)
# Inputs the required shapefile, make sure to change path

shapefile = driver.find_element(By.ID, "shapeFileUpload")
shapefile.send_keys(shapefile_path)
time.sleep(2)

# Finds the desired projection
projection = driver.find_element(By.ID, "projection")
projection.send_keys("Native Projection")
time.sleep(2)

# Clicks on the desired projection, and adds it
projection.send_keys(Keys.ENTER)

print("Select desired data, type something in the console, then enter")
x = input()

time.sleep(3)

# Loops for the desired number of days
for i in range(yearCount):

    for j in range(startMonth, endMonth + 1):
        endDay = days[j]
        if j == 2:
            if checkLeap(startYear):
                endDay = 29

        for k in range(1, endDay + 1):
            # Names the file based on the i index
            driver.find_element(By.ID, "taskName").send_keys(("{monthName}_{day}_{year}").format(monthName = months[j],day = (str(k)).zfill(2),year = str(startYear)))

            # Sets the start date to the i index
            driver.find_element(By.ID, "startDate").send_keys(("{month}-{day}-{year}").format(day = (str(k)).zfill(2), month = (str(j)).zfill(2), year = str(startYear)))

            # Sets the end date to the i index
            text = driver.find_element(By.ID, "endDate")
            text.send_keys(("{month}-{day}-{year}").format(day = (str(k)).zfill(2), month = (str(j)).zfill(2), year = str(startYear)))

            # Submits the request
            text.send_keys(Keys.ENTER)
            time.sleep(3)
            # Waits until the request is submitted.  Based on speed, this can be increased/decreased
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/app-root/div/app-alert/p/ngb-alert')))

            # Clears all of the text fields
            driver.find_element(By.ID, "taskName").clear()
            driver.find_element(By.ID, "startDate").clear()
            driver.find_element(By.ID, "endDate").clear()

    startYear += 1

while True:
    pass
