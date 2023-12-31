SIS Report Downloader
Overview
The SIS Report Downloader is a Python script with a graphical user interface (GUI) built using Tkinter. It provides functionality to download reports from a specified website, organize them, and merge them into a consolidated file. The script utilizes Selenium for web automation and Pandas for data manipulation.
Features
1.	Calendar Picker: Allows users to select a date using a calendar widget.
2.	Store Name Buttons: Fifteen buttons corresponding to different stores initiate the download of reports specific to each store.
3.	Quick Data Button: Automates the login and data download process for all stores in a loop.
4.	Move Button: Organizes downloaded CSV files into a folder named with the current date.
5.	Merge Button: Combines all downloaded CSV files into a single consolidated file.
Prerequisites
•	Python 3.x
•	Tkinter
•	Selenium
•	Pandas
•	ChromeDriver (ensure it is downloaded and its path is correctly specified in the script)
Usage
1.	Run the script using Python.
bashCopy code
python tkinterSWv1.2.py
2.	The GUI will appear, providing options to select a date and perform various tasks.
3.	Use the calendar to navigate to the desired date.
4.	Click on store buttons, Quick Data, Move, or Merge as needed.
5.	Like Utilize the Quick Data button to automate data downloads.
6.	Use the Move button to organize files into a folder with the current date.
7.	Merge downloaded files using the Merge button for comprehensive analysis.
8.	Monitor the console for progress messages and wait for completion alerts.
9.	But if any login Fails then the separate file can be downloaded via <store name> buttons rather than running the whole loop again. 
Configuration
•	Ensure ChromeDriver is downloaded and its path is correctly specified in the script.
•	Update SIS_ID and SIS_PASSWORD lists with valid credentials.
Contributors
•	ItzzInfinity
•	Prasad.anjan25@gmail.com
