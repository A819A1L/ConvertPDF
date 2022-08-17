#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tabula-py


# In[2]:


# Import modules 
import tabula
from PyPDF2 import PdfFileReader


# In[ ]:


pdf_path = "/file path/INV000001.pdf"

# Read PDF File (this contain a list)
df = tabula.read_pdf(pdf_path, pages = 1)[0]
  
# Convert into Excel File
df.to_excel('/file path/INV000001.xlsx')


# In[ ]:




