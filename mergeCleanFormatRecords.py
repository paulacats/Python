#this script separates the csv files depending on if the email field is empty
#then it joins the separate files using the CUSTOMER_ID field
#then it removes the empty, duplicate columns
#finally, it fixes the telephone number formatting

import csv
from pandas import merge, read_csv
import pandas as pd
import os

#here are the column names
#column names/positions, initial extract fields ["DS_ID","CUSTOMER_ID","CUSTOMER_NAME","FIRST_NAME","LAST_NAME","COUNTRY_CODE","CONTACT_TYPE","PHONE_COUNTRY_CODE","PHONE_AREA_CODE","PHONE_NUMBER","EXTENSION","PHONE_TYPE","CONTACT_PURPOSE","EMAIL_ADDRESS","STATUS_FLAG","VALID_PHONE_FLAG","VALID_EMAIL_FLAG","PRIMARY_FLAG"]
#column names/positions, merged file [DS_ID_x,CUSTOMER_ID,CUSTOMER_NAME_x,FIRST_NAME_x,LAST_NAME_x,COUNTRY_CODE_x,CONTACT_TYPE_x,PHONE_COUNTRY_CODE_x,PHONE_AREA_CODE_x,PHONE_NUMBER_x,	EXTENSION_x,PHONE_TYPE_x,CONTACT_PURPOSE_x,EMAIL_ADDRESS_x,STATUS_FLAG_x,VALID_PHONE_FLAG_x,VALID_EMAIL_FLAG_x,PRIMARY_FLAG_x,DS_ID_y,CUSTOMER_NAME_y,FIRST_NAME_y,LAST_NAME_y,COUNTRY_CODE_y,CONTACT_TYPE_y,PHONE_COUNTRY_CODE_y,PHONE_AREA_CODE_y,PHONE_NUMBER_y,EXTENSION_y,PHONE_TYPE_y,CONTACT_PURPOSE_y,EMAIL_ADDRESS_y,STATUS_FLAG_y,VALID_PHONE_FLAG_y,VALID_EMAIL_FLAG_y,PRIMARY_FLAG_y]
#column names/positions, cleaned file[DS_ID_x,CUSTOMER_ID,CUSTOMER_NAME_x,FIRST_NAME_x,LAST_NAME_x,EMAIL_ADDRESS_x,COUNTRY_CODE_y,PHONE_COUNTRY_CODE_y,PHONE_AREA_CODE_y,PHONE_NUMBER_y	EXTENSION_y,PHONE_TYPE_y]


#set the directory to cleanedData folder
os.chdir('cleanedData')
#check number of files in dir
numFiles = (len([name for name in os.listdir('.') if os.path.isfile(name)]))
#stop script if more than one file in directory
if numFiles > 1:
        print("Exiting... can only clean 1 file at a time.")
        exit()

#create file names using source file name
fileName = os.listdir('.')
sourceFile = str(fileName)[2:-6]
csvFilename =  sourceFile + ".csv"
csvFilenameEmail = sourceFile + "_email.csv"
csvFilenamePhone = sourceFile + "_phone.csv"

#-------------------------------
#separate the records into separate files based on contents of email and phone fields 
#---------------------------------

#set up csv file content arrays
csvRowsEmail = []
csvRowsPhone = []

print("Beginning...")

# Read the CSV file in
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
i = 0
for row in readerObj:
        if i == 0:
                csvRowsPhone.append(row)  #append the header row automatically
        if row[13] == "" and row[9] != "": #if email field is empty and phone field is not
                csvRowsPhone.append(row)
        else:
                csvRowsEmail.append(row)
        i = i + 1
csvFileObj.close()

# Write out the CSV files
csvFileObj = open(csvFilenameEmail, 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRowsEmail:
        csvWriter.writerow(row)
csvFileObj.close()
csvFileObj = open(csvFilenamePhone, 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRowsPhone:
        csvWriter.writerow(row)
csvFileObj.close()

#---------------------------------
#merge the files
#---------------------------------

#join the files on CUSTOMER_ID
a = pd.read_csv(csvFilenameEmail, encoding='latin_1', low_memory=False)
b = pd.read_csv(csvFilenamePhone, encoding='latin_1', low_memory=False)
merged = a.merge(b, how='outer', on='CUSTOMER_ID') #outer join using CUSTOMER_ID field
mergeFile = 'merged_' + csvFilename
merged.to_csv(mergeFile, index=False)

#---------------------------------
#move merged fields so that all records have the same data in the same column 
#---------------------------------

csvRowsRefinedMerge = []
# Read the CSV file in
csvFileObj = open(mergeFile)
readerObj = csv.reader(csvFileObj)
disID = ""
custName = ""
fName = ""
lName = ""

for row in readerObj:
        disID = row[18]
        custName = row[19]
        fName = row[20]
        lName = row[21]        
       
        if row[0] == "" and row[2] == "" and row[3] == "" and row[4] == "":       
                row[0] = disID
                row[18] = ""
                row[2] = custName
                row[19] = ""
                row[3] = fName
                row[20] = ""
                row[4] = lName
                row[21] = ""
                csvRowsRefinedMerge.append(row)
        else:
                csvRowsRefinedMerge.append(row)
       
csvFileObj.close()

# Write out the CSV file
csvFileObj = open(mergeFile, 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRowsRefinedMerge:
        csvWriter.writerow(row)
csvFileObj.close()

#---------------------------------
#remove the empty and duplicate columns
#---------------------------------
data = pd.read_csv(mergeFile, encoding='latin_1', low_memory=False)
keep_cols = ['DS_ID_x', 'CUSTOMER_ID', 'CUSTOMER_NAME_x', 'FIRST_NAME_x', 'LAST_NAME_x', 'EMAIL_ADDRESS_x', 'COUNTRY_CODE_y', 'PHONE_COUNTRY_CODE_y', 'PHONE_AREA_CODE_y', 'PHONE_NUMBER_y', 'EXTENSION_y', 'PHONE_TYPE_y']
new_data = data[keep_cols]
new_data.to_csv(mergeFile, index=False)
#https://stackoverflow.com/questions/7588934/deleting-columns-in-a-csv-with-python

#---------------------------------
#fix phone number formatting
#---------------------------------

csvRows = []
csvFileObj = open(mergeFile)
readerObj = csv.reader(csvFileObj)
i = 0
for row in readerObj:                    
        phone = str(row[8])
        phoneLast4 = str(row[9])
        countryCode = str(row[7])                
        if countryCode == "1.0":
                row[7] = 1
        if len(phone) > 7 and i != 0:
                areaCode = phone[1:4]
                townCode = phone[6:9]
                row[8] = areaCode
                row[9] = townCode + phoneLast4
                csvRows.append(row)                
        else:
                csvRows.append(row)               
        i = i + 1
csvFileObj.close()

# Write out the CSV file.
finalOutput = 'FINAL_'+ csvFilename
csvFileObj = open(finalOutput, 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
        csvWriter.writerow(row)
csvFileObj.close()

#---------------------------------
#clean up the directory
#---------------------------------
os.remove(csvFilenameEmail)
os.remove(csvFilenamePhone)
os.remove(mergeFile)

print("All set.")

