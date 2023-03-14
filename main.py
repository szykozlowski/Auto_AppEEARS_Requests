# Import necessary Selenium libraries
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# !!!!!!! CHANGE TO USERNAME/PASSWORD TO APPEARS !!!!!!!

username = ""
password = ""

# Open a chrome window that links to the APPEARS website

ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://appeears.earthdatacloud.nasa.gov/task/area")

# Inputs username and password

driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.NAME,"commit").click()
time.sleep(5)

# Starts a new request

button = driver.find_element(By.XPATH,("//img[@class='thumbnail ng-star-inserted']"))
button.click()
time.sleep(2)

# Path to shapefile

shapefile_path = "Switzerland_Shapefile_Data.zip"

# Inputs the required shapefile, make sure to change path

shapefile = driver.find_element(By.ID,"shapeFileUpload")
shapefile.send_keys(shapefile_path)

# Finds the desired component
driver.find_element(By.ID, "product").send_keys(("wue"))
time.sleep(1)

# Clicks on the desired component
button = driver.find_element(By.XPATH,("//button[@class='dropdown-item active ng-star-inserted']"))
button.click()
time.sleep(1)

# Finds the desired projection
projection = driver.find_element(By.ID,"projection")
projection.send_keys("Geographic")
time.sleep(1)

# Clicks on the desired projection, and adds it
projection.send_keys(Keys.ENTER)
button = driver.find_element(By.XPATH,"//*[@id='top']/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[3]/div[1]/div[2]/div[2]")
button.click()
time.sleep(3)

# Loops for the desired number of days
for i in range(1,30):

    # Names the file based on the i index
    driver.find_element(By.ID,"taskName").send_keys(("June_{}").format((str(i)).zfill(2)))

    # Sets the start date to the i index
    driver.find_element(By.ID,"startDate").send_keys(("03-{}-2023").format((str(i)).zfill(2)))

    # Sets the end date to the i index
    text = driver.find_element(By.ID,"endDate")
    text.send_keys(("03-{}-2023").format((str(i)).zfill(2)))

    # Submits the request
    text.send_keys(Keys.ENTER)

    # Waits until the request is submitted.  Based on speed, this can be increased/decreased
    time.sleep(15)

    # Clears all of the text fields
    driver.find_element(By.ID,"taskName").clear()
    driver.find_element(By.ID,"startDate").clear()
    driver.find_element(By.ID,"endDate").clear()

while True:
    pass