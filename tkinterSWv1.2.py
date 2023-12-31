# to make the software
# import PyInstaller
import sys
# to make the GUI

import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import Calendar
from tkinter.font import Font
from tkinter import messagebox
from tkinter import * #type:ignore
# moving the files into the folder

import os.path
import shutil,glob
from datetime import date
import time as t
from array import * #type:ignore
# to combining CSV files

import pandas as pd

# to login to accounts

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

try:
    ## prints the date
    td = date.today() # Use the today method and assign it to the td variable.  
    print(" Get the today date in Python is: ", td)  
    # creating the folder in todays name
    # Directory 
    directory = str(td)
    # Parent Directory path 
    parent_dir = "C:\\Users\\ANJAN\\Downloads\\"
    
    # Path 
    path = os.path.join(parent_dir, directory)
    # making folder
    os.mkdir(path) 
        # prefs = {"download.default_directory" : path} 
        # options.add_experimental_option("prefs",prefs) 
except FileExistsError:
     pass

def on_button_click(store):
    print(f"Button {store} clicked!")
    seleniumLoginTry(store)
    messagebox.showinfo("SIS Report Downloader says", f"Wait for few seconds {store} Report is downloading")
    
def on_date_pick():
    # picked_date = date_picker.get()
    # print(f"Picked Date: {picked_date}")
    print(cal.get_date())

def seleniumLoginTry(store):   
    # to hold the chrome after the execution is done
    options = webdriver.ChromeOptions()
    

    ## Making the download Url to by getting the date from input by user
    str1="https://ltesd.telesonic.in:8443/store/cpeInventoryReport?s="
    date = cal.get_date()
    print(date)
    str3="&e="
    print ("String 1:",str1)
    print ("String 2:",date)
    downloadUrl=str1+date+str3+date
    print("Concatenated two different strings:",downloadUrl)
    
    arrayElement = 0
    for element in store_names:
        if element==store:
            arrayId= arrayElement
            print(arrayElement)
            break
        arrayElement +=1 


    options.add_experimental_option('detach', True)
    #specify the path to chromedriver.exe (download and save on your computer)
    driver = webdriver.Chrome(options=options, service=Service("C:/chromedriver_win32/chromedriver.exe"))
    
    #open the webpage
    driver.get("https://ltesd.telesonic.in:8443/store/login")
    # find username/email field and send the username itself to the input field
    driver.find_element("id", "username").send_keys(SIS_ID[arrayElement])
    # find password input field and insert password as well
    driver.find_element("id", "password").send_keys(SIS_PASSWORD[arrayElement])

    # # Closes the driver
    # driver.close()

    # click login button
    # driver.find_element(By.PARTIAL_LINK_TEXT, "Login").click()
    driver.find_element(By.CSS_SELECTOR, "input[value='Login'][type='submit']").click()  # final working line

    #wait until the login is done
    t.sleep(3)
    # element = WebDriverWait(ChromeDriverManager, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout")))
    driver.get(downloadUrl)

    #wait until the DOWNLOAD is done
    t.sleep(2)
    # Logging out
    driver.find_element(By.PARTIAL_LINK_TEXT,"Logout").click()

def excelCombine():  #some time combines sometime not try to resolve 
    print("all ok")
    td = date.today()
     # Directory 
    directory = str(td)
    # Parent Directory path 
    parent_dir = "C:\\Users\\ANJAN\\Downloads\\"
    # specifying the path to csv files
    path = parent_dir + directory # path need to change
    # csv files in the path
    files = glob.glob(path + "/*.csv")
    # defining an empty list to store
    # content
    data_frame = pd.DataFrame()
    content = []
    # checking all the csv files in the
    # specified path
    for filename in files:
        # reading content of csv file
        # content.append(filename)
        df = pd.read_csv(filename, index_col=None)
        content.append(df)

    # converting content to data frame
    data_frame = pd.concat(content)
    #to locate this user ID and change the corresponding column name as the name from DB comes as NWCC which need to be vhanged at the final out put
    data_frame.loc[ data_frame["WIMS_ID"] == "IHNAB04", 'SUB Store'] ="Beharampore"
    data_frame.loc[ data_frame["WIMS_ID"] == "IHNFH02", 'SUB Store'] ="Haldia"
    data_frame.loc[ data_frame["WIMS_ID"] == "BGIRI01", 'SUB Store'] ="Port Blair"
    new_path = path + "\\" + "myFile1.csv"
    data_frame.to_csv(new_path, index=False) # path need to change

def AfterDownloadMoveToFolder():
    folder_path = 'C:\\Users\\ANJAN\\Downloads'
    # newPath = 'C:\\Users\\ANJAN\\Downloads\\2023-06-09'
    file_type = r'\*csv'

    td = date.today() # Use the today method and assign it to the td variable.  
    print(" Get the today date in Python is: ", td)  
    # creating the folder in todays name
    # Directory 
    directory = str(td)
    # Parent Directory path 
    parent_dir = "C:\\Users\\ANJAN\\Downloads\\"
    
    for i in range(15):
        files = glob.glob(folder_path + file_type)
        max_file = max(files, key=os.path.getmtime)
        # print(max_file)
        myFile = os.path.basename(max_file).split('/')[-1]
        # print(myFile)
        new_path = parent_dir + directory + "\\" + myFile
        print(new_path)
        shutil.move(max_file, new_path)

def sotreDataWithForLoop():
    options = webdriver.ChromeOptions()
    td = cal.get_date()
    ## Making the download Url to by getting the date from input by user
    str1="https://ltesd.telesonic.in:8443/store/cpeInventoryReport?s="
    str3="&e="
    print ("String 1:",str1)
    print ("String 2:",td)
    downloadUrl=str1+td+str3+td
    print("Concatenated two different strings:",downloadUrl)

    options.add_experimental_option('detach', True)
    #specify the path to chromedriver.exe (download and save on your computer)
    driver = webdriver.Chrome(options=options, service=Service("C:/chromedriver_win32/chromedriver.exe"))
    #open the webpage
    driver.get("https://ltesd.telesonic.in:8443/store/login")
    #     store_names = [
    #    "Asansol","Baharampore", "Haldia","Howrah", "Jalpaiguri",
    #     "Kalyani", "Kharagpur", "Mukandapur", "New Alipur", "Port Blair",
    #     "Rajarhat","Ranaghat/Park Circus", "Nimta", "Salt Lake", "Siliguri",  
    # ]
    SIS_ID =    [ 
            "SDAS-11","IHNAB04","IHNFH02","BCHAT02","ACHAK02",
            "JMAJU03","SPKUM02","PUSHP03","ASIL-01 ","BGIRI01",
            "TDAS01","RDEBN01","NGHOS01","AGHOS02","ASAH-01"]
    SIS_PASSWORD =  [
            "Air@S77857","AIR@NA7128","AIR@NF4596","Air@K59380","Air@M11211",
            "Air@J95342","Air@UM7550","Air@P54824","Air@A69931","AIR@BG6137",
            "AIR@TD9338","Air@P62212","Air@R33447","Air@A34500","Air@A41439"]

    for i in range(15):
        # find username/email field and send the username itself to the input field
        driver.find_element("id", "username").send_keys(SIS_ID[int(i)])
        # find password input field and insert password as well
        driver.find_element("id", "password").send_keys(SIS_PASSWORD[int(i)])

        # click login button
        
        driver.find_element(By.CSS_SELECTOR, "input[value='Login'][type='submit']").click()  # final working line

        #wait until the login is done

        t.sleep(3)
        # element = WebDriverWait(ChromeDriverManager, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout")))
        
        driver.get(downloadUrl)
        
        #wait until the DOWNLOAD is done
        t.sleep(3)

        # Logging out
        driver.find_element(By.PARTIAL_LINK_TEXT,"Logout").click()
    driver.close()

#from Stackover flow to make exe from it
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)




root = tk.Tk()
root.geometry("650x500")
root.title("SIS Report Downloader")
root.configure(bg="#D3F4FB")

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#D3F4FB")
button_frame.pack(pady=10)

# Define the names of the stores for the buttons
store_names = [
   "Asansol","Baharampore", "Haldia","Howrah", "Jalpaiguri",
    "Kalyani", "Kharagpur", "Mukandapur", "New Alipur", "Port Blair",
    "Rajarhat","Ranaghat/Park Circus", "Nimta", "Salt Lake", "Siliguri",  
]
# 1	ASANSOL	                    SDAS-11	    Air@S77857
# 2	BAHARAMPORE              	IHNAB04	    AIR@NA7128
# 3	HALDIA	                    IHNFH02	    AIR@NF4596
# 4	HOWRAH	                    BCHAT02	    Air@K59380
# 5	JALPAIGURI	                ACHAK02	    Air@M11211
# 6	KALYANI	                    JMAJU03	    Air@J95342
# 7	KHARAGPUR	                SPKUM02	    Air@UM7550
# 8	MUKANDAPUR	                PUSHP03	    Air@P54824
# 9	NEW ALIPUR	                ASIL-01 	Air@A69931
# 10 PORT BLAIR	                BGIRI01	    AIR@BG6137
# 11 RAJARHAT	                TDAS01	    AIR@TD9338
# 12 RANAGHAT	                RDEBN01  	Air@P62212
# 13 RISHRA	                    NGHOS01	    Air@R33447
# 14 SALT LAKE	                AGHOS02	    Air@A34500
# 15 SILIGURI	                ASAH-01	    Air@A41439 
## RANAGHAT REMOVED NEED TO BE ADDED // AS THE USERID/ PWD WAS WRONG
# STORE_NAME = 	{'ASANSOL','BAHARAMPORE','HALDIA','HOWRAH','JALPAIGURI','KALYANI','KHARAGPUR','MUKANDAPUR','NEW ALIPUR','PORT BLAIR','RAJARHAT','RANAGHAT','RISHRA','SALT LAKE','SILIGURI'}
SIS_ID =    [ 
            "SDAS-11","IHNAB04","IHNFH02","BCHAT02","ACHAK02",
            "JMAJU03","SPKUM02","PUSHP03","ASIL-01 ","BGIRI01",
            "TDAS01","RDEBN01","NGHOS01","AGHOS02","ASAH-01"]
SIS_PASSWORD =  [
    "Air@S77857","AIR@NA7128","AIR@NF4596","Air@K59380","Air@M11211",
    "Air@J95342","Air@UM7550","Air@P54824","Air@A69931","AIR@BG6137",
    "AIR@TD9338","Air@P62212","Air@R33447","Air@A34500","Air@A41439"]


buttons = []
row_count = 0
column_count = 0

# Create 15 blue buttons with store names in a grid layout
for i in range(15):
    store = store_names[i]
    button = tk.Button(button_frame, text=store, bg="#59D7EE", fg="black",font=Font(family="Times New Roman"), command=lambda btn=store: on_button_click(btn))
    button.grid(row=row_count, column=column_count, padx=5, pady=5)
    buttons.append(button)

    column_count += 1
    if column_count >= 5:
        column_count = 0
        row_count += 1

# Create a calendar datepicker
# Create calendar
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd", cursor="hand1")
cal.pack()

# Create a button to print the picked date
date_button = tk.Button(root, text="Select Date",bg="#87ACA3",fg="black", font=Font(family="Trebuchet MS", weight="bold"), command=on_date_pick)
date_button.pack(pady=10)

# Create the remaining 3 buttons ("Jack", "Jones", "Jill") side by side
additional_buttons_frame = tk.Frame(root, bg="#D3F4FB")
additional_buttons_frame.pack()

additional_buttons = [ "Quick Data 😎","Move","Merge"]

# for name in additional_buttons:
# button = tk.Button(additional_buttons_frame, text=name, bg="#A5CFE3", fg="black",font=Font(family="Times New Roman"), command=lambda btn=name: AfterDownloadMoveToFolder())
# button.pack(side=tk.LEFT, padx=5, pady=5)
# buttons.append(button)

button = tk.Button(additional_buttons_frame, text=additional_buttons[int(0)], bg="#A5CFE3", fg="black",font=Font(family="Times New Roman"), command=sotreDataWithForLoop)
button.pack(side=tk.LEFT, padx=5, pady=5)
buttons.append(button)

button1 = tk.Button(additional_buttons_frame, text=additional_buttons[int(1)], bg="#A5CFE3", fg="black",font=Font(family="Times New Roman"), command=AfterDownloadMoveToFolder)
button1.pack(side=tk.LEFT, padx=5, pady=5)
buttons.append(button1)

button2 = tk.Button(additional_buttons_frame, text=additional_buttons[int(2)], bg="#A5CFE3", fg="black",font=Font(family="Times New Roman"), command=excelCombine)
button2.pack(side=tk.LEFT, padx=5, pady=5)
buttons.append(button2)
# Create a label at the bottom
# label_text = "© Copyright to Infinite Solutions Inc."
# label = tk.Label(root, text=label_text, bg="#D3F4FB", fg="black", font=Font(family="Designed & developed by Infinity", size=8,slant="italic"), anchor=tk.E)
# label.pack(pady=10)
# label_text2 = "Designed & developed by Infinity"
# label2 = tk.Label(root, text=label_text2, bg="#D3F4FB", fg="black", font=Font(family="Arial", size=8,slant="italic"), justify="right",anchor="e")
# label2.pack()
Label(root, text= "© Copyright to Infinite Solutions Inc.                                                                                                      Designed & developed by Infinity", font=Font(family="Arial", size=8,slant="italic"), background="#D3F4FB").pack(pady=0, side= BOTTOM, anchor="e")
# Label(root, text= " ",font=Font(family="Arial", size=8,slant="italic"), background="#D3F4FB").pack(pady=0, side= BOTTOM, anchor="e")

root.mainloop()
