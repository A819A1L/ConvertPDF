#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tabula-py


# In[2]:


# Import modules 
import tabula
from PyPDF2 import PdfFileReader


# In[3]:


# Get attribute of PDF file
pdf_path = "/Users/adavies/Gardners/DocCentral/Analysis/7. General Operations/3. Transport/4. Invoice Data FY 21/Tuffnells/43INV-03410207.pdf"

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

if __name__ == '__main__':
    path = pdf_path
    extract_information(path)


# In[4]:


# Read PDF file
AllTablesInPDF = tabula.read_pdf(pdf_path, pages = "all")

Counter = 1   
# Convert into excel file
for singleTable in AllTablesInPDF:
    
    singleTable.to_excel('/Users/adavies/Gardners/DocCentral/Analysis/7. General Operations/3. Transport/4. Invoice Data FY 21/Tuffnells/43TuffInvoicev8.xlsx',sheet_name=str(Counter))
    
    Counter = Counter + 1


# In[ ]:




