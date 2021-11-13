import streamlit as st
import os
header = st.container()
dataset = st.container()

import os
import pandas as pd
# import cv2
import glob
import regex as re
# path = 'Assignment/*.pdf'

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

with header:
    st.title('CV names and filenames')

st.write("""
# Upload your folder here!
""")


    # st.write(bytes_data)
lst = []
file_names = []

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    print(uploaded_file)
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    # filenames = os.listdir(folder_path)
    # selected_filename = st.selectbox('Select a file',filenames)
    # return os.path.join(folder_path,selected_filename)

# filename = file_selector()
# st.write('You selected %s' % filename)

    output_string = StringIO()

    # print(f'{file}')
    # print("Assignment/{}".format(file))
    # print(file)
    # output_string = StringIO()
    with open("resumes/{}".format(uploaded_file.name), 'rb') as in_file:
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
        file_names.append(uploaded_file.name)

names_list = ["".join(values) for values in lst]

Cv_list = pd.DataFrame()

Cv_list['names'] = names_list
Cv_list['file_names'] = file_names

# print(Cv_list)

st.table(Cv_list)