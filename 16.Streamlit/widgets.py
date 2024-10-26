import streamlit as st
import pandas as pd


st.title("Streamlit widgets")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:" , 0, 100 , 25)

options = ["python" , "Java" , "C++" , "Javascript"]
choice = st.selectbox("choose your favourite language:" , options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello , {name}")

data = {
    "Name" :["Abhi" , "Shubh" , "mylo" , "Abhishek"],
    "Age"  : [19,20,6,20],
    "City"  : ['New York' , 'Chicago'  , 'Delhi' , 'los Angeles']
}

df = pd.DataFrame(data)
st.write(df)

# upload button
uploaded_file = st.file_uploader("choose a file"  , type=["csv" , "xlsx" , "xls"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(('xls' , 'xlsx')):
        try:
          df = pd.read_excel(uploaded_file)
        except UnicodeDecodeError:
            st.error("Could not decode file. check file type")
    elif uploaded_file.name.endswith('csv'):
        try:
            df = pd.read_csv(uploaded_file, encoding="latin1")  # or "cp1252" if needed
        except UnicodeDecodeError:
            st.error("Could not decode file. Please check the file encoding.")
    else:
        st.error("Unsupported file type.")
else:
    print("File not uploaded")
st.line_chart(df)