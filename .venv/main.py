import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.png", width=600)

with col2:
    st.title("Aleksa Velickovic")
    content = """Tech enthusiast with a small amount of professional experience. I hold a Bachelors degree in Electrical and Computer Engineering at Faculty of Technical Sciences in Novi Sad. I am currently working as a Software System Test Engineer at Continental Automotive. https://github.com/AleksaIT

Beside my work I like to spend my free time for individual researches in various fields of tech and physics, learning new technologies and update myself with the ones I already know (currently working on my personal projects in Python and exercising testing in Selenium Webdriver).

I am very keen to learn and very interested in the tech that will shape our future FOR GOOD."""

    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""

st.write(content2)