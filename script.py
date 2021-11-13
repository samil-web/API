import os
import pandas as pd
import cv2
import glob
import regex as re
from web_app import uploaded_files
# path = 'Assignment/*.pdf'

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

lst = []
file_names = []
output_string = StringIO()
for file in os.listdir('Assignment'):
    # print(f'{file}')
    # print("Assignment/{}".format(file))
    output_string = StringIO()
    with open("Assignment/{}".format(file), 'rb') as in_file:
        # output_string = ''
        # print(file)
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        
        lst.append(re.findall('([A-Z][a-z]*)([\\s\\\'-][A-Z][a-z]*)*',(output_string.getvalue().title()))[0])
        file_names.append(file)

names_list = ["".join(values) for values in lst]

Cv_list = pd.DataFrame()

Cv_list['names'] = names_list
Cv_list['file_names'] = file_names

print(Cv_list)