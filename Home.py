import requests
import streamlit as st
from datetime import date

api_key = st.secrets["my_api_key"]

# Make request
@st.cache_data(ttl=86400)
def get_apod_data(api_key, date=None):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    if date:
        url += f"&date={date}"
    response = requests.get(url)
    return response.json()


# WebSite/WebApp to output the Astronomy Photo of the Day
st.set_page_config(layout="centered")
st.header(':rainbow[NASA Astronomy Picture of the Day] :moon:')

# Date picker for user to select date
selected_date = st.date_input("Select a date", value=date.today())

# Fetch the APOD data
data = get_apod_data(api_key, selected_date)

# Display the data
if "media_type" in data and data["media_type"] == "video":
    st.video(data["url"], format="video/mp4")
elif "hdurl" in data:
    st.image(data["hdurl"], caption=data["title"])
    st.subheader(data["title"])
else:
    st.write("No image or video available for this date.")

st.write(data.get("explanation", "No explanation available."))


st.text("Copyright: " + data["copyright"] + " " +  data["date"])

