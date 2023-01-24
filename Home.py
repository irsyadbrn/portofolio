import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photos.jpg", width=335)

with col2:
    st.title("Irsyad Barran")
    content = """
        Hello, I am Irsyad Barran. i graduated from Binus University majoring Information System. Right now i continue my study for my master degree in Binus University. The major that I choose is  Information System Management, because i still want to broaden my knowledge about IT.
        
        I have 1 year experience as an IT staff at PT. Synerga Tata Internasional, subsidiary of BUMN called  PT. Surveyor Indonesia. I also have an experience as an admin at PT. Glory Bumi Nusantara. And my recent experience, I work at PT. Kawan Baru Teknologi as an IT Staff. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.3, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")