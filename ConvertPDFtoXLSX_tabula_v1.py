#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tabula-py


# In[2]:


# Import modules 
import tabula
from PyPDF2 import PdfFileReader


# In[ ]:


pdf_path = "/Users/adavies/Gardners/DocCentral/Analysis/7. General Operations/3. Transport/4. Invoice Data FY 21/Tuffnells/43INV-03410207.pdf"

# Read PDF File (this contain a list)
df = tabula.read_pdf(pdf_path, pages = 1)[0]
  
# Convert into Excel File
df.to_excel('/Users/adavies/Gardners/DocCentral/Analysis/7. General Operations/3. Transport/4. Invoice Data FY 21/Tuffnells/43TuffInvoicev9.xlsx')


# In[ ]:




