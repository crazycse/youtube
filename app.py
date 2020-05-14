import streamlit as st
st.title("Youtube Video Downloader")
#st.write("GOKUL")
#st.markdown("*This app is in it's early stages!* Will be updated regularly.")
user_input = st.text_input("Enter link to download", '')
import os
import pyqrcode  
from pyqrcode import QRCode

import requests
some_url = user_input

temp=False

try:
    resp = requests.get(some_url)
    if resp.status_code == 200:
       print("OK")
       temp=True
    else:
       print("Not OK")
except :
    st.write(" Try Again")

if temp:
    s = 'youtube-dl '+user_input
    os.system(s)
    url = pyqrcode.create(s) 
    url.png('myqr.png', scale = 6)

    from PIL import Image

    image = Image.open("myqr.png")

    st.image(image, caption='QR',use_column_width=True)

    l=os.listdir()

    for i in l:
        if i[-3:]=="mp4":
            break

    video_file = open(i, 'rb')

    video_bytes = video_file.read()

    st.video(video_bytes)
elif user_input=='':
    st.write("Enter link")
else:
    st.write("INVALID")
