# Overview

Appears (https://appeears.earthdatacloud.nasa.gov/) is a NASA application that allows users to access a large geospatial database.  The application restricts the maximum amount of data a user can receice per request, which makes getting large files quite tedious.  This code automates the process, and requests specified data for a specified timeframe.  Presents the user with a GUI, from where the desired set of dates/years is entered.  Input is then handled through Selenium, which scrapes the website for required text fields.
