# Overview

AppEEARS (https://appeears.earthdatacloud.nasa.gov/) is a web-based NASA application that allows users to access a large geospatial database.  The application restricts the maximum amount of data a user can receive per request, which makes getting large spatial files quite tedious.  This code automates the process, and requests spatial (not point) data over a specific time period and geographic extent.  This code presents the user with a GUI, from which the desired set of dates/years. Geographic extent is specified using a shapefile that must be put in the same directory as the python file.  Input is then handled through Selenium, which scrapes the appEEARS website for required text fields.

The code has been tested on Windows and Mac platforms. 

# User Guide

## Step 1:

Download Chromedriver for your respective operating system. (https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.24/)

![chromedriv](https://user-images.githubusercontent.com/92408910/234077946-e1bd893f-b64c-45af-9e2a-f10f8fc75be2.PNG)

## Step 2:

Rename your shapefile "Shapefile", and put it in the same directory as the Python file.

![direct](https://user-images.githubusercontent.com/92408910/234078748-8681b8c7-73e8-4518-82fe-52724c560031.PNG)

## Step 3: 

Run the program, and input your AppEEARS login info, and desired temporal range of data.  The optimal delay will vary between machines, so tune it as needed.  

![AppEEARSSSSSSS](https://user-images.githubusercontent.com/92408910/234077387-63e819b3-7817-4ada-bbb1-e158d2511746.PNG)
