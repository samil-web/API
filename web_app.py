import streamlit as st

header = st.container()
dataset = st.container()

with header:
    st.title('CV names and filenames')

st.write("""
# Upload your folder here!
""")

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

st.download_button(
    label="Download data as CSV",
    data='csv',
    file_name='large_df.csv',
    mime='text/csv',)
