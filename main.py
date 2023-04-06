# Import necessary Selenium libraries
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import os


# Gets Variables Entered into Text Fields
def getTextFields(user,passw,start, end,years,yearStart):
    global username
    global password
    global startMonth
    global endMonth
    global startYear
    global yearCount
    username = user.get()
    password = passw.get()
    startMonth = int(start.get())
    endMonth = int(end.get())
    startYear = int(yearStart.get())
    yearCount = int(years.get())
    root.destroy()

root = tk.Tk()
userText = tk.StringVar()
passText = tk.StringVar()
monthStartText = tk.StringVar()
monthEndText= tk.StringVar()
yearCountText = tk.StringVar()
yearStartText = tk.StringVar()

root.geometry("900x500")
root.title("this APPEEARS to be useful")

# Username Text Box
userLabel = tk.Label(root,text="Username:")
usernameBox = tk.Entry(root,font='Arial',textvariable=userText)
userLabel.grid(row=0,column=0,padx=100,pady=10)
usernameBox.grid(row=0,column=1)

# Password Text Box
passLabel = tk.Label(root,text="Password:")
passwordBox = tk.Entry(root,font='Arial',textvariable=passText,show="*")
passLabel.grid(row=1,column=0,padx=100,pady=10)
passwordBox.grid(row=1,column=1)

# Start Month Text Box
monthStartLabel = tk.Label(root,text="Start Month:")
monthStartBox = tk.Entry(root,font='Arial',textvariable=monthStartText)
monthStartLabel.grid(row=2,column=0,padx=100,pady=10)
monthStartBox.grid(row=2,column=1)

# End Month Text Box
monthEndLabel = tk.Label(root,text="End Month:")
monthEndBox = tk.Entry(root,font='Arial',textvariable=monthEndText)
monthEndLabel.grid(row=3,column=0,padx=100,pady=10)
monthEndBox.grid(row=3,column=1)

# Start Year Text Box
yearStartLabel = tk.Label(root,text="Start Year:")
yearStartBox = tk.Entry(root,font='Arial',textvariable=yearStartText)
yearStartLabel.grid(row=4,column=0,padx=100,pady=10)
yearStartBox.grid(row=4,column=1)

# Year Count Text Box
yearCountLabel = tk.Label(root,text="Year Count:")
yearCountBox = tk.Entry(root,font='Arial',textvariable=yearCountText)
yearCountLabel.grid(row=5,column=0,padx=100,pady=10)
yearCountBox.grid(row=5,column=1)


# Go! Button
button = tk.Button(root, text = "Go!",command=lambda: getTextFields(usernameBox,passwordBox,monthStartBox,monthEndBox,yearCountBox,yearStartBox))
button.grid(row=7,column=1)

root.mainloop()

# Check if Leap Year
def checkLeap(year):
    if(year % 4 == 0):
        return True
    return False

# Lists of Month Names and Corresponding Days
months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Open a chrome window that links to the APPEARS website

ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://appeears.earthdatacloud.nasa.gov/task/area")

# Inputs username and password

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "commit").click()
time.sleep(5)

# Starts a new request

button = driver.find_element(By.XPATH, ("//img[@class='thumbnail ng-star-inserted']"))
button.click()
time.sleep(2)

# Path to shapefile
working_directory = os.getcwd()
file_path = working_directory + "Switzerland_Shapefile_Data.zip"
shapefile_path = "Switzerland_Shapefile_Data.zip"
shapefile_path = os.path.join(working_directory,shapefile_path)
# Inputs the required shapefile, make sure to change path

shapefile = driver.find_element(By.ID, "shapeFileUpload")
shapefile.send_keys(shapefile_path)

# Finds the desired component
driver.find_element(By.ID, "product").send_keys(("wue"))
time.sleep(1)

# Clicks on the desired component
button = driver.find_element(By.XPATH, ("//button[@class='dropdown-item active ng-star-inserted']"))
button.click()
time.sleep(1)

# Finds the desired projection
projection = driver.find_element(By.ID, "projection")
projection.send_keys("Geographic")
time.sleep(1)

# Clicks on the desired projection, and adds it
projection.send_keys(Keys.ENTER)
button = driver.find_element(By.XPATH,
                             "//*[@id='top']/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[3]/div[1]/div[2]/div[2]")
button.click()
time.sleep(3)

# Loops For the Desired Number of Years
for i in range(yearCount):

    # Loops Through the Selected Months
    for j in range(startMonth, endMonth + 1):
        endDay = days[j]

        # If February, Check Leap Year
        if j == 2:
            if checkLeap(startYear):
                endDay = 29

        # Loops For the Amount of Days in Current Month
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

            # Waits until the request is submitted.  Based on speed, this can be increased/decreased
            time.sleep(20)

            # Clears all of the text fields
            driver.find_element(By.ID, "taskName").clear()
            driver.find_element(By.ID, "startDate").clear()
            driver.find_element(By.ID, "endDate").clear()

    startYear += 1

while True:
    pass
