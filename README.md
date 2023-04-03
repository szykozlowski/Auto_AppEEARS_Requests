# Overview

appEEARS (https://appeears.earthdatacloud.nasa.gov/) is a web-based NASA application that allows users to access a large geospatial database.  The application restricts the maximum amount of data a user can receive per request, which makes getting large files quite tedious.  This code automates the process, and requests data over a specific time period and geographic extent.  This code presents the user with a GUI, from which the desired set of dates/years and geographic extents are entered.  Input is then handled through Selenium, which scrapes the appEEARS website for required text fields.

The code has been tested on Windows and Mac platforms. 
