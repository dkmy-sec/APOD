import requests
import streamlit as st

api_key = "TF4OHxmlQC89n13wuSmNQCluhezSlmJPV3OAbh6k"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary of the data
data = request.json()

# WebSite/WebApp to output the Astronomy Photo of the Day
st.set_page_config(layout="centered")

# Get image from request and import to readable format for Streamlit
image_url = data["hdurl"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(data["title"])
st.image(image_filepath)
st.write(data["explanation"])

