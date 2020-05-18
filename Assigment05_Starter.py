# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AAsgekar,5.18.2020,Added code to complete the program
# AAsgekar,5.18.2020,Added comments to script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
fileHandle = open(objFile, "r")
for row in fileHandle:
    strData = row.split(",")
    dicRow = {"Task":strData[0].strip(),"Priority":strData[1].strip()} #create dictionary row
    lstTable.append(dicRow) #append row to list
fileHandle.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your current data is:")
        print("Task, Priority")
        for row in lstTable:
            print(row["Task"]+", "+row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("What is your task? ")
        priority = input("What is the priority level? ")
        dicRow = {"Task":task.capitalize(), "Priority":priority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        i = None #variable to determine which statement to print
        rmvTask = input("What task would you like to remove? ")
        for row in lstTable:
            if row["Task"].lower() == rmvTask.lower():
                lstTable.remove(row)
                i = True
            else:
                i = False

        if i == True:
            print("The task " + rmvTask.capitalize() + " has been removed.")
        else:
            print("That task is not in your To Do list.")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        fileHandle = open(objFile, "w")
        for row in lstTable:
            fileHandle.write(row["Task"]+", "+row["Priority"] + "\n")
        fileHandle.close()
        print("Your data has been saved.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Thank you for using this program. \nPress the enter key to exit.")
        break  # and Exit the program
