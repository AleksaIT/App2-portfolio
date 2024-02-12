import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.png")

with col2:
    st.title("Aleksa Velickovic")
    content = """Hi, I am Aleksa. I am a System Test Engineer, Python developer and a good person."""

    st.info(content)