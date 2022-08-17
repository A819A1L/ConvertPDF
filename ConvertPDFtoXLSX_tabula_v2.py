# Version 1
import tabula
import pandas as pd

pdf_name = "/file path/INV000001.pdf"
ExcelOutputPath = "/file path/INV000001.xlsx" # to save each page as individual file

FinalFileName = "/file path/INV000001.xlsx"

dfAllPages = tabula.read_pdf(pdf_name, pages='all')

dfMergedData = pd.DataFrame()

counter = 0

for singlePage in dfAllPages:
   
    dfSinglePage = tabula.read_pdf(pdf_name, pages='all')[counter]

    ExcelFileName = ExcelOutputPath + str(counter) + '.xlsx' # to save each page as individual file
    print (counter)

    # EXPORT AN INDIVIDUAL PAGE
    dfSinglePage.to_excel(ExcelFileName) # to save each page as individual file

    #MERGE THE SINGLE PAGE INTO A COMBINED DATAFRAME
    dfMergedData = dfMergedData.append(dfSinglePage,ignore_index=True)

    #EXPORT THE COMBINED DATAFRAME
    dfMergedData.to_excel(FinalFileName)
    
    counter = counter + 1
 

# Versio 2
# This code takes empty rows out before exporting to excel
import tabula
import pandas as pd
pdf_name = "/file path/INV000001.pdf"
FinalFileName = "/file path/INV000001.xlsx"
dfAllPages = tabula.read_pdf(pdf_name, pages='all')
dfMergedData = pd.DataFrame()
dfCleanedData = pd.DataFrame()
counter = 0
for singlePage in dfAllPages:
   
    dfSinglePage = tabula.read_pdf(pdf_name, pages='all')[counter]
    
    print ("Page:" + str(counter + 1))
    # Merge the single page into a combined dataframe
    
    dfMergedData = dfMergedData.append(dfSinglePage,ignore_index=True)
    counter = counter + 1
# Remove any rows where the cell under "account" heading is blank
dfCleanedData = dfMergedData.dropna(subset=["Account"])
 
# Export the clean dataframe
dfCleanedData.to_excel(FinalFileName)


# Version 3
# This code brings up a dialog box to ask you to pick a file to convert so you don't have to hard code the pdf file into your script
import tabula
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
pdf_name = askopenfilename()
FinalFileName = "/file path/INV000001.xlsx" # Assign name
dfAllPages = tabula.read_pdf(pdf_name, pages='all')
dfMergedData = pd.DataFrame()
dfCleanedData = pd.DataFrame()
counter = 0
for singlePage in dfAllPages:
   
    dfSinglePage = tabula.read_pdf(pdf_name, pages='all')[counter]
    
    print ("Page:" + str(counter + 1))
    # Merge the single page into a combined dataframe
    dfMergedData = dfMergedData.append(dfSinglePage,ignore_index=True)
    counter = counter + 1
# Remove any rows where the cell under "account" heading is blank     
dfCleanedData = dfMergedData.dropna(subset=["Account"])
 
# Export the clean dataframe
dfCleanedData.to_excel(FinalFileName)



