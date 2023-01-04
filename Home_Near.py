# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Near MegaDashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('Near Dashboard')

# Content
c1, c2 = st.columns(2)
c1.image(Image.open('Images/3.png'))


st.subheader('Introduction')
st.write("""

Mostafa Will Provide this text in the Future

""")
